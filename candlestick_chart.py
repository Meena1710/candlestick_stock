import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

# Define time frame
print("Using yfinance")
start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

# Load data using yfinance
data = yf.download('ITC.BO', start=start, end=end)

# Print the data to check its structure
print(data)

# Keep only the relevant columns: 'Open', 'High', 'Low', 'Close', and 'Volume'
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

# Visualization using mplfinance
mpf.plot(
    data, 
    type='candle', 
    style='charles', 
    title='ITC Ltd (BO)', 
    volume=True, 
    mav=(10,20),  # Moving averages
    figratio=(12,8), 
    figscale=1.2
)

print(data.head())
