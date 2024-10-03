import requests
import concurrent.futures
from colorama import Fore, Style, init
import pyfiglet  # For the banner

# Initialize colorama
init(autoreset=True)

# Function to print the banner
def print_banner():
    banner = pyfiglet.figlet_format("CORS Checker", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.MAGENTA + Style.BRIGHT + "Author: madtiger")
    print(Fore.MAGENTA + "Telegram: @DevidLuice")
    print(Fore.LIGHTBLACK_EX + "-" * 60 + "\n")

# Function to check CORS headers and potential XSS
def check_cors_and_xss(url):
    try:
        headers = {'Origin': 'http://evil.com'}
        response = requests.get(url, headers=headers, timeout=5, verify=True)  # Timeout and SSL verification

        cors_header = response.headers.get('Access-Control-Allow-Origin')
        if cors_header:
            if 'evil.com' in cors_header:
                return {
                    'url': url,
                    'status': 'vulnerable',
                    'message': (Fore.RED + Style.BRIGHT + f"[*] {url}\n" +
                                Fore.RED + Style.BRIGHT + "[!] CORS misconfiguration detected!\n" +
                                Fore.RED + f"    └─ Access-Control-Allow-Origin: {cors_header}\n" +
                                Fore.LIGHTBLACK_EX + "-" * 60)
                }
            else:
                return {
                    'url': url,
                    'status': 'not_vulnerable',
                    'message': (Fore.GREEN + Style.BRIGHT + f"[*] {url}\n" +
                                Fore.GREEN + Style.BRIGHT + "[+] CORS header found, but not vulnerable.\n" +
                                Fore.GREEN + f"    └─ Access-Control-Allow-Origin: {cors_header}\n" +
                                Fore.LIGHTBLACK_EX + "-" * 60)
                }
        else:
            return {
                'url': url,
                'status': 'not_vulnerable',
                'message': (Fore.YELLOW + Style.BRIGHT + f"[*] {url}\n" +
                            Fore.YELLOW + "[!] No CORS header found.\n" +
                            Fore.LIGHTBLACK_EX + "-" * 60)
            }

    except requests.exceptions.RequestException as e:
        return {
            'url': url,
            'status': 'error',
            'message': (Fore.RED + Style.BRIGHT + f"[*] {url}\n" +
                        Fore.RED + "[!] Error occurred during request:\n" +
                        Fore.RED + f"    └─ {url}\n" +
                        Fore.LIGHTBLACK_EX + "-" * 60)
        }

# Load the websites from a file and ensure they have the proper scheme
def load_websites(filename):
    try:
        with open(filename, 'r') as file:
            websites = [line.strip() for line in file]
            # Add http:// or https:// if not present
            for i in range(len(websites)):
                if not websites[i].startswith(('http://', 'https://')):
                    websites[i] = 'http://' + websites[i]
            return websites
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + f"[!] File {filename} not found.")
        return []

# Function to check multiple websites concurrently with 20 threads
def check_cors_and_xss_for_websites(filename, max_threads=20):
    websites = load_websites(filename)
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_url = {executor.submit(check_cors_and_xss, url): url for url in websites}
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                result = future.result()
                results.append(result)
                print(result['message'])  # Print each result with styled output
            except Exception as exc:
                print(Fore.RED + f"[!] Generated an exception for {future_to_url[future]}: {url}")

    # Save the results into separate files
    with open('vulnerable_urls.txt', 'w') as vuln_file, open('not_vulnerable_urls.txt', 'w') as not_vuln_file:
        for result in results:
            if result['status'] == 'vulnerable':
                vuln_file.write(result['url'] + '\n')
            elif result['status'] == 'not_vulnerable':
                not_vuln_file.write(result['url'] + '\n')

# Run the script with user input
if __name__ == "__main__":
    # Print the banner
    print_banner()

    # Ask the user for the websites file path
    filename = input(Fore.CYAN + Style.BRIGHT + "Enter File : ")
    check_cors_and_xss_for_websites(filename)
