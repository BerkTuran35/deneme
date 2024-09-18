import requests
import hmac
import hashlib
import time
import json

# API key ve secret bilgilerinizi buraya girin
api_key = 'gGtQaOuDGgNEZB73Hq'
api_secret = 'BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD'  # Bu değeri kendi secret key'inizle değiştirin

url = "https://api.bybit.com/v5/order/cancel"

# Current timestamp (milliseconds)
timestamp = str(int(time.time() * 1000))
recv_window = '20000'

# Payload bilgileri
payload = {
    "category": "linear",
    "symbol": "ETHUSDT",
    "OrderLinkId": "xxx-6"
    "orderId": "xxx-6",  # Geçerli bir orderId kullanın
    "orderFilter": "Order"
}

# Payload'ı JSON formatına dönüştür
payload_str = json.dumps(payload, separators=(',', ':'))

# İmza hesaplama fonksiyonu
def generate_signature(api_secret, timestamp, recv_window, payload_str):
    param_str = f"{timestamp}{api_key}{recv_window}{payload_str}"
    return hmac.new(api_secret.encode('utf-8'), param_str.encode('utf-8'), hashlib.sha256).hexdigest()

# İmza hesapla
signature = generate_signature(api_secret, timestamp, recv_window, payload_str)

# Headers bilgileri
headers = {
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': recv_window,
    'X-BAPI-SIGN': signature,
    'Content-Type': 'application/json'
}

# POST isteği gönder
response = requests.post(url, headers=headers, data=payload_str)

# Yanıtı yazdır
print(response.text)
