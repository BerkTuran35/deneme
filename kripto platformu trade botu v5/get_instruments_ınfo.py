from pybit.unified_trading import HTTP

# Bybit API oturumunu oluşturun
session = HTTP(testnet=False, api_key="YOUR_API_KEY", api_secret="YOUR_SECRET_KEY")

# API çağrısı yapın
try:
    response = session.get_index_price_kline(
        category="linear",  # Geçerli kategori
        symbol="BTCUSDT",
        interval="1",  # 1 dakikalık interval (string formatında)
        start=1670601600000,  # Başlangıç zaman damgası (milisaniye cinsinden)
        end=1670608800000,  # Bitiş zaman damgası (milisaniye cinsinden)
        limit=2
    )
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")
