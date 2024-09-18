from pybit.unified_trading import HTTP
session = HTTP(
    testnet=False,
    api_key="gGtQaOuDGgNEZB73Hq",
    api_secret="BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD",
)
print(session.set_leverage(
    category="linear",
    symbol="ETHUSDT",
    buyLeverage="10",
    sellLeverage="6",
))