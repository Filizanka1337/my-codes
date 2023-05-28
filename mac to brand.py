import requests

mac_address = input("Enter the MAC address: ")

url = f"https://api.maclookup.app/v2/macs/{mac_address}/company/name"
try:
    response = requests.get(url)
    response.raise_for_status()
    company = response.text.strip()
    print(f"The manufacturer of this device is: {company}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while looking up the MAC address: {e}")