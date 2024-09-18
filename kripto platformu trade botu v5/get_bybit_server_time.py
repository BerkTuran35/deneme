import requests

# API uç noktası
url = "https://api.bybit.com/v5/market/time"

# İstek için gerekli parametreler (boş, çünkü bu endpoint parametre gerektirmiyor)
params = {}

# İstek gönderimi
response = requests.get(url, headers={}, params=params)

# Yanıtı yazdırın
print(response.text)
