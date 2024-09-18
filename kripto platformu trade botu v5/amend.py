import requests
import time
import hashlib
import hmac
import json

url = "https://api.bybit.com/v5/order/amend"

# Güncel zaman damgasını oluştur
timestamp = str(int(time.time() * 1000))  # milisaniye cinsinden zaman damgası
recv_window = '20000'

# Payload verileri
payload = {
  "category": "linear",
    "symbol": "ETHUSDT",
    "isLeverage": 1,
    "side": "Buy",
    "orderType": "Market",
    "qty": "0.2",
    "price": " 4 ",
    "triggerPrice": None,
    "triggerDirection": None,
    "triggerBy": None,
    "orderFilter": "order",
    "orderIv": None,
    "timeInForce": "GTC",
    "positionIdx": 0,
    "orderId": "ccdcfb3f-1126-4d9c-b8a2-b98e3df879d9"
    "orderLinkId": "deneme-1116",
    "takeProfit": "2700",
    "stopLoss": "2260",
    "tpTriggerBy": None,
    "slTriggerBy": None,
    "reduceOnly": False,
    "closeOnTrigger": False,
    "smpType": None,
    "mmp": None,
    "tpslMode": None,
    "tpLimitPrice": None,
    "slLimitPrice": None,
    "tpOrderType": None,
    "slOrderType": None
}

# JSON stringine dönüştür
payload_str = json.dumps(payload)

# API anahtarlarınız
api_key = 'gGtQaOuDGgNEZB73Hq'
api_secret = 'BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD'  # Bu kısmı kendi API Secret'inizle değiştirin

# İmzayı oluştur
param_str = f"{timestamp}{api_key}{recv_window}{payload_str}"
signature = hmac.new(api_secret.encode('utf-8'), param_str.encode('utf-8'), hashlib.sha256).hexdigest()

# Header verileri
headers = {
  'X-BAPI-API-KEY': api_key,
  'X-BAPI-TIMESTAMP': timestamp,
  'X-BAPI-RECV-WINDOW': recv_window,
  'X-BAPI-SIGN': signature,
  'Content-Type': 'application/json'
}

# İsteği gönder
response = requests.post(url, headers=headers, data=payload_str)

# Yanıtı yazdır
print(response.text)
