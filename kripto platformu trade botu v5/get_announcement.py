from pybit.unified_trading import HTTP
session = HTTP(testnet=False)
print(session.get_announcement(
    locale="en-US",
    limit=1,
))