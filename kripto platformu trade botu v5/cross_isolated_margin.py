import requests
import time
import hmac
import hashlib
import json

# API anahtarlarınızı ve gizli anahtarınızı buraya ekleyin
api_key = 'gGtQaOuDGgNEZB73Hq'
api_secret = 'BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD'  # Gizli anahtarınızı buraya ekleyin

# İstek URL'si ve yükü
url = "https://api.bybit.com/v5/position/switch-isolated"
payload = {
    "category": "linear",
    "symbol": "BTCUSDT",
    "tradeMode": 0,  # 0: isolated, 1: cross
    "buyLeverage": "10",
    "sellLeverage": "10"
}

# Zaman damgası
timestamp = str(int(time.time() * 1000))

# Parametreleri birleştirme
params = f"api_key={api_key}&timestamp={timestamp}&recv_window=20000&{json.dumps(payload, separators=(',', ':'))}"

# İmza hesaplama
sign = hmac.new(api_secret.encode(), params.encode(), hashlib.sha256).hexdigest()

# Header bilgileri
headers = {
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': '20000',
    'X-BAPI-SIGN': sign
}

# POST isteği gönderme
response = requests.post(url, headers=headers, json=payload)

# Yanıtı yazdırma
print(response.text)
