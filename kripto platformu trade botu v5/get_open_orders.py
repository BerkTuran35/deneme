from pybit.unified_trading import HTTP
session = HTTP(
    testnet=False,
    api_key="gGtQaOuDGgNEZB73Hq",
    api_secret="BwWXdxZ81XCrg3TUp855IVBCCTwguFJ9J8wD",
)
print(session.get_open_orders(
    category="linear",
    symbol="ETHUSDT",
    openOnly=0,
    limit=1,
))