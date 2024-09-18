import requests
import time
import hmac
import hashlib
import json
import urllib.parse

def get_position_info(testnet=False):
    api_key = "vaRDbtQa20BeCM0De0"
    api_secret = "nqxCt3AQmyFoE22bOLmgMo65uKeUfWQlJVvp"
    
    timestamp = int(time.time() * 1000)
    params = {
        "category": "linear",
        "symbol": "ETHUSDT"
    }
    
    # Generate signature
    param_str = '&'.join([f"{key}={urllib.parse.quote(str(value))}" for key, value in sorted(params.items())])
    sign_str = f"{timestamp}{api_key}5000{param_str}"
    signature = hmac.new(
        bytes(api_secret, 'utf-8'),
        sign_str.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    # Prepare headers
    headers = {
        "X-BAPI-API-KEY": api_key,
        "X-BAPI-SIGN": signature,
        "X-BAPI-SIGN-TYPE": "2",
        "X-BAPI-TIMESTAMP": str(timestamp),
        "X-BAPI-RECV-WINDOW": "5000",
        "Content-Type": "application/json"
    }
    
    # Choose URL based on testnet flag
    base_url = "https://api.bybit.com" if testnet else "https://api.bybit.com"
    url = f"{base_url}/v5/position/list"
    
    print(f"Sending request to: {url}")
    print(f"Headers: {json.dumps(headers, indent=2)}")
    print(f"Params: {json.dumps(params, indent=2)}")
    print(f"Sign string: {sign_str}")
    
    # Send request
    response = requests.get(url, headers=headers, params=params)
    
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {json.dumps(dict(response.headers), indent=2)}")
    
    if response.status_code == 200:
        data = response.json()
        print("Position Information:")
        print(json.dumps(data, indent=2))
        return data
    else:
        print(f"Error: {response.status_code}")
        print(f"Response Text: {response.text}")
        return None

if __name__ == "__main__":
    use_testnet = False  # Set this to True if you want to use testnet
    get_position_info(use_testnet)