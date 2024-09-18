import hmac
import hashlib
import json

# API credentials
api_key = 'gGtQaOuDGgNEZB73Hq'
api_secret = 'BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD'  # Replace with your actual API secret

# Parameters
timestamp = '1658385579423'
recv_window = '5000'
raw_request_body = {"category": "option"}

# Convert raw_request_body to JSON string
raw_request_body_str = json.dumps(raw_request_body, separators=(',', ':'))

# Create the string to be signed
param_str = f"{timestamp}{api_key}{recv_window}{raw_request_body_str}"

# Generate the signature
def generate_signature(api_secret, param_str):
    return hmac.new(api_secret.encode('utf-8'), param_str.encode('utf-8'), hashlib.sha256).hexdigest()

signature = generate_signature(api_secret, param_str)

# Output
print("Timestamp:", timestamp)
print("API Key:", api_key)
print("Recv Window:", recv_window)
print("Raw Request Body:", raw_request_body_str)
print("Signature:", signature)
