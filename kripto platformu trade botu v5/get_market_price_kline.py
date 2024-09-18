import requests

# API uç noktası
url = "https://api.bybit.com/v5/market/mark-price-kline"

# İstek için gerekli parametreler (örnek)
params = {
    "symbol": "BTCUSDT",
    "interval": "1D",  # Örneğin günlük veriler
    "start": "1670601600000",  # Başlangıç zaman damgası
    "end": "1670608800000"     # Bitiş zaman damgası
}

# İstek gönderimi
response = requests.get(url, headers={}, params=params)

# Yanıtı yazdırın
print(response.text)
