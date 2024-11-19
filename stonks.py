#! /usr/bin/env python

import yfinance as yf
import datetime as dt
# Get data for Microsoft, Apple and Google
df = yf.download(['MSFT', 'AAPL', 'GOOG'], period = "1d", interval="1m")
filename = "Close Data " + dt.datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
df["Close"].to_csv(filename)

#Note: make this file user executable...  the shebang at the start specifies how it is to be run .