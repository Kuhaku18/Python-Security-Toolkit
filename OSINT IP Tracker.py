# OSINT IP Tracker - A reconnaissance tool that queries an external API to geolocate target IP addresses.
import requests
while True:
    target_ip = input("Enter IP add:")
    url = f"http://ip-api.com/json/{target_ip}"
    data = requests.get(url).json()
    if data["status"] == "fail":
        print("Invaild IP!")
    else:
        print(data["country"])
        print(data["regionName"])
        print(data["zip"])
        print(data["city"])
        print(data["isp"])
        break