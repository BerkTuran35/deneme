import requests

url = "https://api.bybit.com/v5/market/insurance"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)