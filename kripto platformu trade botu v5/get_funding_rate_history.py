from pybit.unified_trading import HTTP
import tkinter as tk
from tkinter import messagebox
session = HTTP()
url = "https://api.bybit.com/v5/market/funding/history"

print(session.get_funding_rate_history(
    category="linear",
    symbol="ETHUSDT",
    limit=1,
))