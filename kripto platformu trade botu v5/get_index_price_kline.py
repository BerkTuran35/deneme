import requests

# API uç noktası
url = "https://api.bybit.com/v5/market/index-price-kline"

# İstek için gerekli parametreler
params = {
    "category": "linear",
    "symbol": "BTCUSDT",
    "interval": "1D",
    "start": "1670601600000",
    "end": "1670608800000",
}

# İstek gönderimi
response = requests.get(url, headers={}, params=params)

# Yanıtı yazdırın
print(response.text)
