import hmac
import hashlib
import time

# API credentials
api_key = 'gGtQaOuDGgNEZB73Hq'
api_secret = 'BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD'  # Replace with your actual API secret

# Parameters
timestamp = str(int(time.time() * 1000))
recv_window = '5000'
query_string = 'category=linear&symbol=BTCUSDT'

# Create the string to be signed
param_str = f"{timestamp}{api_key}{recv_window}{query_string}"

# Generate the signature
def generate_signature(api_secret, param_str):
    return hmac.new(api_secret.encode('utf-8'), param_str.encode('utf-8'), hashlib.sha256).hexdigest()

signature = generate_signature(api_secret, param_str)

# Output
print("Timestamp:", timestamp)
print("API Key:", api_key)
print("Recv Window:", recv_window)
print("Query String:", query_string)
print("Signature:", signature)
