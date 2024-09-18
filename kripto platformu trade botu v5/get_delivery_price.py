import requests

url = "https://api.bybit.com/v5/market/delivery-price"

# Doğru kategori ve sembol parametrelerini kullanın
params = {
    "category": "linear",  # Kategori parametresi doğru olmalı
    "symbol": "BTC"    # Geçerli bir sembol kullanın
}

response = requests.get(url, params=params)
print(response.json())
