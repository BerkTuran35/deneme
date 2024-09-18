from pybit.unified_trading import HTTP
session = HTTP(testnet=False)
print(session.get_open_interest(
    category="inverse",
    symbol="BTCUSD",
    intervalTime="5min",
    startTime=1669571100000,
    endTime=1669571400000,
))