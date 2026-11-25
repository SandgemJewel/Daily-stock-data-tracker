import csv
import datetime as dt
import yfinance as yf
date = dt.date.today()
spx = yf.Ticker("^GSPC")
tmr = date + dt.timedelta(days=1)
# 1. Fetch intraday data (end is exclusive, so add 1 day)
hist = spx.history(start=date, end=tmr, interval="1m")

# 2. Filter to your specific time range (in the exchange's local timezone, America/New_York)
window = hist.between_time("09:30", "10:30")

# 3. Calculate the high and low for that window
window_high = round(window["High"].max(), 2)
window_low = round(window["Low"].min(), 2)


# 4. Do the same with all the stats
daily_high = round(hist["High"].max(),2)
daily_low = round(hist["Low"].min() ,2)


opening = round(hist["Open"].iloc[0], 2)
# opening = round(spx.info['open'], 2)
close = round(hist['Close'].iloc[-1], 2)



print(f"High (9:30–10:30 AM): {window_high:.2f}")
print(f"Low  (9:30–10:30 AM): {window_low:.2f}")
print(f'daily high: {daily_high:.2f}')
print(f'daily low: {daily_low:.2f}')
print(f"daily open: {spx.info['open']}")
print(f"daily close: {hist['Close'].iloc[-1]:.2f}")
print(date)

with open('data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([str(date), str(window_high), str(window_low), str(daily_high), str(daily_low), str(opening), str(close)])


#attemtpting to push, fr this time idk this is yapping abt
