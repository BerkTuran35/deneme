import requests
import time
import hmac
import hashlib
import json
import urllib.parse

API_KEY = "vaRDbtQa20BeCM0De0"
API_SECRET = "nqxCt3AQmyFoE22bOLmgMo65uKeUfWQlJVvp"
BASE_URL = "https://api.bybit.com"  # Use "https://api-testnet.bybit.com" for testnet

def generate_signature(params, timestamp):
    param_str = json.dumps(params)
    sign_str = f"{timestamp}{API_KEY}5000{param_str}"
    return hmac.new(bytes(API_SECRET, 'utf-8'), sign_str.encode('utf-8'), hashlib.sha256).hexdigest()

def http_request(method, endpoint, params=None):
    url = f"{BASE_URL}{endpoint}"
    timestamp = str(int(time.time() * 1000))
    
    if params is None:
        params = {}
    
    signature = generate_signature(params, timestamp)
    
    headers = {
        "X-BAPI-API-KEY": API_KEY,
        "X-BAPI-SIGN": signature,
        "X-BAPI-SIGN-TYPE": "2",
        "X-BAPI-TIMESTAMP": timestamp,
        "X-BAPI-RECV-WINDOW": "5000",
        "Content-Type": "application/json"
    }
    
    print(f"Request URL: {url}")
    print(f"Request Headers: {json.dumps(headers, indent=2)}")
    print(f"Request Params: {json.dumps(params, indent=2)}")
    print(f"Sign String: {timestamp}{API_KEY}5000{json.dumps(params)}")
    
    if method == "GET":
        response = requests.get(url, headers=headers, params=params)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=params)
    else:
        raise ValueError("Unsupported HTTP method")
    
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {json.dumps(dict(response.headers), indent=2)}")
    print(f"Response Content: {response.text}")
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def get_open_positions():
    endpoint = "/v5/position/list"
    params = {
        "category": "linear",
        "symbol": "ETHUSDT"
    }
    return http_request("GET", endpoint, params)

def close_position(symbol, side, qty):
    endpoint = "/v5/order/create"
    params = {
        "category": "linear",
        "symbol": symbol,
        "side": side,
        "orderType": "Market",
        "qty": str(qty),
        "reduceOnly": True,
        "closeOnTrigger": True
    }
    return http_request("POST", endpoint, params)

def main():
    positions = get_open_positions()
    print(f"Full API Response for Positions: {json.dumps(positions, indent=2)}")
    
    if positions and positions.get('retCode') == 0 and 'result' in positions and 'list' in positions['result']:
        open_positions = [position for position in positions['result']['list'] if float(position['size']) != 0]
        if open_positions:
            for position in open_positions:
                side = "Sell" if position['side'] == "Buy" else "Buy"
                qty = position['size']
                symbol = position['symbol']
                print(f"Closing Position: Symbol: {symbol}, Side: {side}, Quantity: {qty}")
                result = close_position(symbol, side, qty)
                if result:
                    print(f"Close order result: {json.dumps(result, indent=2)}")
                time.sleep(1)  # Add a small delay between orders
        else:
            print("No open positions found.")
    else:
        print("Failed to retrieve position data or unexpected API response format.")

if __name__ == "__main__":
    main()