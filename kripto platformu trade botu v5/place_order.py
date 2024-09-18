import requests
import hmac
import hashlib
import time
import json

# API credentials
api_key = 'vaRDbtQa20BeCM0De0'
api_secret = 'nqxCt3AQmyFoE22bOLmgMo65uKeUfWQlJVvp'  # Replace with your actual API secret

# API URL
url = "https://api.bybit.com/v5/order/create"

# Current timestamp (milliseconds)
timestamp = str(int(time.time() * 1000))
recv_window = '20000'

# Request payload
payload = {
    "category": "linear",
    "symbol": "ETHUSDT",
    "isLeverage": 10,
    "side": "Sell",
    "orderType": "Market",
    "qty": "0.1",
    "price": "5",
    "triggerPrice": None,
    "triggerDirection": None,
    "triggerBy": None,
    "orderFilter": None,
    "orderIv": None,
    "timeInForce": "GTC",
    "positionIdx": 0,
    "orderLinkId": "xxxx-523222342333323534",
    "takeProfit": "",
    "stopLoss": "",
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

# Convert payload to JSON string
payload_str = json.dumps(payload, separators=(',', ':'))

# Generate signature
def generate_signature(secret, timestamp, recv_window, payload_str):
    param_str = f"{timestamp}{api_key}{recv_window}{payload_str}"
    return hmac.new(secret.encode('utf-8'), param_str.encode('utf-8'), hashlib.sha256).hexdigest()

# Generate the signature
signature = generate_signature(api_secret, timestamp, recv_window, payload_str)

# Headers
headers = {
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': recv_window,
    'X-BAPI-SIGN': signature,
    'Content-Type': 'application/json'
}

# Make the POST request
response = requests.post(url, headers=headers, data=payload_str)

# Output the response
print(response.status_code)
print(response.text)
