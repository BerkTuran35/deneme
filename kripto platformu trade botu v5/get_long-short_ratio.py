import requests

url = "https://api.bybit.com/v5/market/account-ratio"

payload = {
    "symbol": "BTCUSDT",  # Geçerli bir symbol kullanın
    "category": "linear"  # Geçerli bir category kullanın
}
headers = {
    "X-BYBIT-API-KEY": "YOUR_API_KEY",
    "X-BYBIT-API-SIGN": "YOUR_API_SIGNATURE",
    "X-BYBIT-API-TIMESTAMP": "YOUR_API_TIMESTAMP",
}

response = requests.request("GET", url, headers=headers, params=payload)

print(response.text)
