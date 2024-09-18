import requests
import time
import hmac
import hashlib
import json

# API anahtarlarınızı ve gizli anahtarınızı buraya ekleyin
api_key = 'gGtQaOuDGgNEZB73Hq'
api_secret = 'BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD'

# İstek URL'si ve yükü
url = "https://api.bybit.com/v5/position/switch-mode"
payload = {
    "category": "linear",
    "symbol": "ETHUSDT",
    "coin": "USDT",
    "mode": "1"  # 0: isolated, 1: cross
}

# Zaman damgası
timestamp = str(int(time.time() * 1000))

# Parametreleri birleştirme
payload_str = json.dumps(payload, separators=(',', ':'))
params = f"api_key={api_key}&timestamp={timestamp}&recv_window=20000&{payload_str}"

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
