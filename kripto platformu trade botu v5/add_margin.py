import requests
import time
import hmac
import hashlib
import json

# API bilgileri
api_key = "gGtQaOuDGgNEZB73Hq"
api_secret = "BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD"
url = "https://api.bybit.com/v5/order/create"

# İmza oluşturma fonksiyonu
def generate_signature(api_secret, timestamp, recv_window, payload_str):
    param_str = f"{timestamp}{api_key}{recv_window}{payload_str}"
    return hmac.new(api_secret.encode('utf-8'), param_str.encode('utf-8'), hashlib.sha256).hexdigest()

# Pozisyon kapatma fonksiyonu
def close_position(symbol, current_position_side, qty):
    """
    Açık pozisyonu kapatmak için ters yönlü bir emir gönderir.
    """
    url = "https://api.bybit.com/v5/order/create"
    timestamp = str(int(time.time() * 1000))
    recv_window = '5000'
    
    # Pozisyon yönüne göre ters yönlü bir emir oluşturur
    if current_position_side == "Buy":
        side = "Sell"
    elif current_position_side == "Sell":
        side = "Buy"
    else:
        print("Invalid position side!")
        return
    
    # Market emri ile pozisyonu kapatma isteği
    payload = {
        "category": "linear",
        "symbol": symbol,
        "side": side,
        "orderType": "Market",
        "qty": qty,
        "timeInForce": "GTC",
    }

    payload_str = json.dumps(payload)
    signature = generate_signature(api_secret, timestamp, recv_window, payload_str)

    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': timestamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': signature,
        'Content-Type': 'application/json'
    }

    # POST isteği gönder
    response = requests.post(url, headers=headers, data=payload_str)
    return response.json()

# Örnek kullanım
symbol = "ETHUSDT"
current_position_side = "Buy"  # Açık pozisyon yönü
qty = "0.1"  # Kapatılacak miktar

response = close_position(symbol, current_position_side, qty)
print(response)
