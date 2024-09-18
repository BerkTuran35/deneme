import requests

# API uç noktası
url = "https://api.bybit.com/v5/market/recent-trade"

# Geçerli bir sembol ile parametreler
params = {
    "symbol": "BTCUSDT"  # Örnek geçerli sembol
}

# İstek gönderimi
response = requests.get(url, headers={}, params=params)

# Yanıtı yazdırın
print(response.text)
