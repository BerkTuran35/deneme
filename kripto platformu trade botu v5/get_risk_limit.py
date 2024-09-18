import requests

# API Endpoint URL'si
url = "https://api.bybit.com/v5/market/risk-limit"

# Parametreler (kategori geçerli bir değerle güncellenmeli)
params = {
    "category": "linear",  # Doğru kategori değeri
    "symbol": "BTCUSDT"   # İlgili sembol (opsiyonel)
}

# Header bilgileri (varsa eklenir)
headers = {
    "X-BYBIT-APIKEY": "YOUR_API_KEY",  # API anahtarınızı buraya ekleyin
    "X-BYBIT-SIGNATURE": "YOUR_SIGNATURE",  # İmzanızı buraya ekleyin (gerekli ise)
    "Content-Type": "application/json"
}

# API çağrısı
response = requests.get(url, headers=headers, params=params)

# Yanıtı JSON formatında al
data = response.json()

# Yanıtı ekrana yazdır
print(data)
