from pybit.unified_trading import HTTP
session = HTTP(testnet=False)
print(session.get_historical_volatility(
    category="option",
    baseCoin="ETH",
    period=30,
))