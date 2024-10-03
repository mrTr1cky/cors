Introducing CORS Checker: A Powerful Tool for Detecting CORS Vulnerabilities
Hey security enthusiasts and ethical hackers! Today, I’m excited to introduce a new tool I’ve developed called CORS Checker. It’s designed to help you quickly and efficiently scan websites for CORS (Cross-Origin Resource Sharing) misconfigurations, which can expose sensitive information or lead to potential cross-origin attacks. Let's dive into what the tool does, why you should use it, and how it can help secure your web applications.

What is CORS and Why is it Important?
Before I get into the tool itself, let's do a quick refresher on CORS. CORS is a security mechanism implemented in web browsers that restricts how resources on a web page can be requested from another domain. In simple terms, it prevents unauthorized cross-origin requests from being made. When misconfigured, CORS policies can allow malicious actors to bypass the restrictions, potentially enabling cross-site scripting (XSS) and data exfiltration from users.

When a website doesn't properly enforce CORS policies, it's vulnerable to attacks where a malicious website could interact with sensitive data hosted on another domain without the user's knowledge or permission. This is a critical security issue that every web developer and security researcher needs to address!

Introducing the CORS Checker Tool
What Does CORS Checker Do?
CORS Checker is a Python-based tool that allows you to automatically scan multiple websites for CORS vulnerabilities. Specifically, it checks whether a website improperly allows cross-origin requests from a malicious origin (http://evil.com) in its Access-Control-Allow-Origin header. If the header contains evil.com, the website is flagged as vulnerable to CORS misconfigurations.

With CORS Checker, you can:

Scan massive lists of websites at once.
Detect potential vulnerabilities that attackers could exploit for unauthorized data access.
Save results in organized log files for easy analysis.
Key Features of CORS Checker
Here’s a quick look at what CORS Checker brings to the table:

Multi-threaded Scanning: Perform fast scans using 20 concurrent threads, making it incredibly efficient for large lists of websites.
Automatic URL Formatting: It automatically adds http:// or https:// if the URLs in your list don’t include the scheme, saving you the hassle of editing each one manually.
CORS Misconfiguration Detection: The tool checks for websites that allow http://evil.com in their Access-Control-Allow-Origin header, a clear indication of vulnerability.
Colored Terminal Output: It provides visually engaging, color-coded output, so you can easily differentiate between vulnerable and safe websites.
Detailed Logging: Vulnerable URLs are saved in vulnerable_urls.txt, and non-vulnerable or safe URLs are stored in not_vulnerable_urls.txt. This helps with post-scan analysis.
Stylish Banner and Author Info: The tool even comes with a slick ASCII banner and displays the author's details (that’s me: mad tiger 😎) for a professional touch!
How to Use CORS Checker
Using CORS Checker is incredibly simple. Here's a quick step-by-step guide to getting started:

1. Prepare Your List of URLs
Start by creating a text file (for example, urls.txt) that contains the list of websites you want to scan. Each website should be on a new line, like this:

Copy code
example.com
another-example.com
2. Run the Script
To launch CORS Checker, simply run the script after installing the required dependencies (listed in the GitHub repository):

bash
Copy code
python cors_checker.py
3. Provide the File Path
You’ll be prompted to enter the path to your URL list. For example:

mathematica
Copy code
Enter File : urls.txt
The tool will begin scanning each website in the list for CORS misconfigurations and display the results in the terminal.

4. View the Results
Once the scan is complete, the results will be saved in two files:

vulnerable_urls.txt: URLs that have CORS misconfigurations.
not_vulnerable_urls.txt: URLs that are either safe or don’t include CORS headers.
