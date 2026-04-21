#Directory Buster - An OSINT script that brute-forces hidden website directories by analyzing HTTP status codes.
import requests
target = "http://testphp.vulnweb.com"
wordlist = ["admin", "login", "uploads", "images","secret", "backup"]
for word in wordlist:
    url = f"{target}/{word}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"Found Hidden Directory: {url}")
        else:
            print(f"Not found: {word}")
    except requests.exceptions.Timeout:
        print(f"Timeout: The server took too long to answer for {word}")
    except requests.exceptions.ConnectionError:
        print(f"Connection ERROR: The server is completely down or blocking us!")
        break