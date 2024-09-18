import requests

# API uç noktası
url = "https://api.bybit.com/v5/market/tickers"

# Geçerli parametrelerle isteği yapın
params = {
    "category": "linear"  # veya geçerli bir kategori değeri
}

# İstek gönderimi
response = requests.get(url, headers={}, params=params)

# Yanıtı yazdırın
print(response.text)
