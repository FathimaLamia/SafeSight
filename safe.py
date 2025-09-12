import requests
from colorama import Fore, Style, init
import json
from pyfiglet import Figlet

# Initialize colorama
init(autoreset=True)

def banner():
    f = Figlet(font="slant")
    ascii_banner = f.renderText("SafeSight")
    line = Fore.CYAN + "=" * 60 + Style.RESET_ALL

    print(line)
    print(Fore.CYAN + ascii_banner + Style.RESET_ALL)
    print(Fore.YELLOW + " 🌐 👁️  Website Header Checker  🔒 🛡️\n")
    print(line)

banner()

EXPECTED_SECURITY_HEADERS = [
    'Content-Security-Policy',
    'X-Frame-Options',
    'X-Content-Type-Options',
    'Strict-Transport-Security',
    'Referrer-Policy',
    'Permissions-Policy',
    'Expect-CT',
    'Feature-Policy',  # Deprecated but still sometimes present
]

def fetch_headers(url):
    """
    Fetch headers using HEAD request, fallback to GET if needed.
    """
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        if response.status_code >= 400 or not response.headers:
            response = requests.get(url, allow_redirects=True, timeout=10)
        return {k.lower(): v for k, v in response.headers.items()}
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Error fetching the URL: {e}")
        return {}

def check_headers(url, headers_to_check):
    """
    Check presence of specified HTTP headers on the URL.
    """
    response_headers = fetch_headers(url)
    if not response_headers:
        return None

    missing = []
    present = []
    for header in headers_to_check:
        if header.lower() in response_headers:
            present.append(header)
        else:
            missing.append(header)

    print(Fore.CYAN + f"\nChecked headers for {url}:")
    print(Fore.GREEN + f"Present headers ({len(present)}):")
    for h in present:
        print(Fore.GREEN + f"  - {h}")

    print(Fore.RED + f"\nMissing headers ({len(missing)}):")
    for h in missing:
        print(Fore.RED + f"  - {h}")

    return {"url": url, "present": present, "missing": missing}

def save_results_to_file(results, filename):
    """
    Save header check results to a JSON file.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)
        print(Fore.YELLOW + f"\n[+] Results saved to {filename}")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to save file: {e}")

def main():
    url = input("Enter website URL (with http:// or https://): ").strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        print(Fore.RED + "Please include the protocol (http:// or https://) in the URL.")
        return

    # Ask if user wants to see default headers being checked
    see_list = input("Do you want to see the default security headers that will be checked? (y/n): ").strip().lower()
    if see_list == 'y':
        print(Fore.MAGENTA + "\nDefault security headers checked:")
        for h in EXPECTED_SECURITY_HEADERS:
            print(f" - {h}")

    # Check default headers
    results = check_headers(url, EXPECTED_SECURITY_HEADERS)

    # Ask if user wants to check any other specific headers
    more = input("\nDo you want to check for any other specific headers? (y/n): ").strip().lower()
    if more == 'y':
        user_headers = input("Enter the header names separated by commas (e.g., X-Custom-Header, Server): ").strip()
        if user_headers:
            additional_headers = [h.strip() for h in user_headers.split(',') if h.strip()]
            extra_results = check_headers(url, additional_headers)
            if extra_results:
                results["custom_headers"] = extra_results
        else:
            print(Fore.YELLOW + "No additional headers entered.")

    # Ask to save results
    save_option = input("\nDo you want to save the results to a file? (y/n): ").strip().lower()
    if save_option == 'y':
        filename = input("Enter filename (e.g., results.json): ").strip()
        if not filename:
            filename = "header_check_results.json"
        save_results_to_file(results, filename)

if __name__ == "__main__":
    main()
