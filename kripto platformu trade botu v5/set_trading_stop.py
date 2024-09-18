import time
import hmac
import hashlib
import json
import requests

# API anahtarları ve gizli anahtarlarınızı buraya ekleyin
api_key = "gGtQaOuDGgNEZB73Hq"
api_secret = "BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD"
timestamp = str(int(time.time() * 1000))
recv_window = "20000"

# İstek verilerini tanımlayın
payload = {
    "category": "linear",
    "symbol": "ETHUSDT",
    "takeProfit": "5000",
    "stopLoss": "1000",
    "tpTriggerBy": "MarkPrice",
    "slTriggerBy": "IndexPrice",
    "tpslMode": "Full",
    "tpOrderType": "Market",
    "slOrderType": "Market",
    "tpSize": "50",
    "slSize": "50",
    "tpLimitPrice": None,
    "slLimitPrice": None,
    "positionIdx": 0
}

# Parametreleri JSON formatında hazırlayın
params = json.dumps(payload, separators=(',', ':'))

# İmza hesaplama
def generate_signature(api_secret, timestamp, recv_window, params):
    to_sign = f"{timestamp}{api_key}{recv_window}{params}"
    return hmac.new(api_secret.encode(), to_sign.encode(), hashlib.sha256).hexdigest()

signature = generate_signature(api_secret, timestamp, recv_window, params)

# İstek gönderme
url = "https://api.bybit.com/v5/position/trading-stop"
headers = {
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': recv_window,
    'X-BAPI-SIGN': signature,
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=params)

# Yanıtı yazdırma
print(response.text)
