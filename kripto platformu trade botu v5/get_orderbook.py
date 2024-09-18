from pybit.unified_trading import HTTP

# Bybit API oturumunu oluşturun
session = HTTP(testnet=False)

# Orderbook verilerini alır
response = session.get_orderbook(
    category="linear",
    symbol="BTCUSDT"
)

# Yanıtı yazdırın
print(response)
