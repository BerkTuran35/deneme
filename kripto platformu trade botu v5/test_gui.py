import tkinter as tk
from tkinter import messagebox, Toplevel, Text
import requests
import hmac
import hashlib
import time
import json
import os  # Eksik import
import uuid  # Eksik import

# API credentials
api_key = 'gGtQaOuDGgNEZB73Hq'
api_secret = 'BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD'

# Generate signature for the request
def generate_signature(secret, timestamp, recv_window, payload_str):
    param_str = f"{timestamp}{api_key}{recv_window}{payload_str}"
    return hmac.new(secret.encode('utf-8'), param_str.encode('utf-8'), hashlib.sha256).hexdigest()

# Function to place an order
def place_order(symbol, side, qty, price=None):
    timestamp = str(int(time.time() * 1000))
    recv_window = '20000'
    payload = {
        "category": "linear",
        "symbol": symbol,
        "side": side,  # "Buy" or "Sell"
        "orderType": "Market" if not price else "Limit",
        "qty": qty,
        "price": price if price else None,
        "timeInForce": "GTC" if price else "ImmediateOrCancel",
        "reduceOnly": False,
        "closeOnTrigger": False
    }
    payload_str = json.dumps(payload, separators=(',', ':'))
    signature = generate_signature(api_secret, timestamp, recv_window, payload_str)

    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': timestamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': signature,
        'Content-Type': 'application/json'
    }

    url = "https://api.bybit.com/v5/order/create"
    try:
        response = requests.post(url, headers=headers, data=payload_str)
        response.raise_for_status()
        print("Order Response:", response.status_code)
        print(response.text)
        messagebox.showinfo("Order Placed", f"Order placed successfully for {symbol}!")
    except requests.exceptions.RequestException as e:
        print(f"Error placing order: {e}")
        messagebox.showerror("Order Failed", f"Error placing order: {e}")

# Function to get open positions
def get_open_positions():
    timestamp = str(int(time.time() * 1000))
    recv_window = '20000'
    url = "https://api.bybit.com/v5/position/list"

    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': timestamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': generate_signature(api_secret, timestamp, recv_window, ''),
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data['retCode'] == 0:
            return data['result']
        else:
            print(f"Error fetching positions: {data['retMsg']}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Function to close an order
def close_position(symbol, side, qty):
    timestamp = str(int(time.time() * 1000))
    recv_window = '20000'
    payload = {
        "category": "linear",
        "symbol": symbol,
        "side": side,  # "Buy" to close a sell position or "Sell" to close a buy position
        "orderType": "Market",
        "qty": qty,
        "price": None,
        "timeInForce": "GTC",
        "reduceOnly": True,
        "closeOnTrigger": True
    }
    payload_str = json.dumps(payload, separators=(',', ':'))
    signature = generate_signature(api_secret, timestamp, recv_window, payload_str)

    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': timestamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': signature,
        'Content-Type': 'application/json'
    }

    url = "https://api.bybit.com/v5/order/create"
    try:
        response = requests.post(url, headers=headers, data=payload_str)
        response.raise_for_status()
        print("Order Response:", response.status_code)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error creating order: {e}")

# Function to set trading stop (SL/TP)
def set_trading_stop(symbol, stop_loss=None, take_profit=None):
    timestamp = str(int(time.time() * 1000))
    recv_window = '20000'
    payload = {
        "symbol": symbol,
        "category": "linear",
    }
    
    if stop_loss:
        payload["stopLoss"] = stop_loss
    if take_profit:
        payload["takeProfit"] = take_profit

    payload_str = json.dumps(payload, separators=(',', ':'))
    signature = generate_signature(api_secret, timestamp, recv_window, payload_str)

    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': timestamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': signature,
        'Content-Type': 'application/json'
    }

    url = "https://api.bybit.com/v5/position/trading-stop"
    try:
        response = requests.post(url, headers=headers, data=payload_str)
        response.raise_for_status()
        print("Set Trading Stop Response:", response.status_code)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error setting trading stop: {e}")

# Function to display open positions in a new window
def show_open_positions():
    open_positions = get_open_positions()

    if open_positions:
        position_window = Toplevel(root)
        position_window.title("Open Positions")
        position_window.geometry("400x400")

        # Create a Text widget to display positions
        text_box = Text(position_window, wrap='word', height=20, width=50)
        text_box.pack(pady=10, padx=10)

        # Display the open positions in the Text widget
        for position in open_positions.get('list', []):
            if position['size'] != '0':  # Check if there is an open position
                position_info = f"Symbol: {position['symbol']}\nSize: {position['size']}\nSide: {position['side']}\nEntry Price: {position['entryPrice']}\n\n"
                text_box.insert('end', position_info)
            else:
                text_box.insert('end', "No open positions found.\n")
    else:
        messagebox.showerror("Error", "Failed to retrieve open positions.")

# GUI setup
root = tk.Tk()
root.title("API Key and Order Input")

api_key_label = tk.Label(root, text="API Key:")
api_key_label.pack(pady=(10, 0))
api_key_entry = tk.Entry(root, width=50)
api_key_entry.pack(pady=(0, 10))

api_secret_label = tk.Label(root, text="API Secret:")
api_secret_label.pack(pady=(10, 0))
api_secret_entry = tk.Entry(root, width=50, show='*')
api_secret_entry.pack(pady=(0, 10))

symbol_label = tk.Label(root, text="Symbol (e.g., ETHUSDT):")
symbol_label.pack(pady=(10, 0))
symbol_entry = tk.Entry(root, width=50)
symbol_entry.pack(pady=(0, 10))

side_label = tk.Label(root, text="Side (e.g., Buy or Sell):")
side_label.pack(pady=(10, 0))
side_entry = tk.Entry(root, width=50)
side_entry.pack(pady=(0, 10))

qty_label = tk.Label(root, text="Quantity:")
qty_label.pack(pady=(10, 0))
qty_entry = tk.Entry(root, width=50)
qty_entry.pack(pady=(0, 10))

price_label = tk.Label(root, text="Price (optional):")
price_label.pack(pady=(10, 0))
price_entry = tk.Entry(root, width=50)
price_entry.pack(pady=(0, 10))

tp_label = tk.Label(root, text="Take Profit Price (optional):")
tp_label.pack(pady=(10, 0))
tp_entry = tk.Entry(root, width=50)
tp_entry.pack(pady=(0, 10))

sl_label = tk.Label(root, text="Stop Loss Price (optional):")
sl_label.pack(pady=(10, 0))
sl_entry = tk.Entry(root, width=50)
sl_entry.pack(pady=(0, 10))

# Save API keys to keys.py
def save_keys(api_key, api_secret):
    if not api_key or not api_secret:
        messagebox.showerror("Error", "API Key and Secret must not be empty.")
        return

    with open("keys.py", "w") as f:
        f.write(f'api_key = "{api_key}"\n')
        f.write(f'api_secret = "{api_secret}"\n')
    messagebox.showinfo("Success", "API keys saved successfully!")

save_button = tk.Button(root, text="Save API Keys", command=lambda: save_keys(api_key_entry.get(), api_secret_entry.get()))
save_button.pack(pady=(10, 5))

# Add button to place order
order_button = tk.Button(root, text="Place Order", command=lambda: place_order(symbol_entry.get(), side_entry.get(), qty_entry.get(), price_entry.get()))
order_button.pack(pady=(10, 5))

# Button to set SL/TP
set_stop_button = tk.Button(root, text="Set SL/TP", command=lambda: set_trading_stop(symbol_entry.get(), sl_entry.get(), tp_entry.get()))
set_stop_button.pack(pady=(10, 5))

# Button to show open positions
open_positions_button = tk.Button(root, text="Show Open Positions", command=show_open_positions)
open_positions_button.pack(pady=(10, 5))

root.mainloop()
