import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('AAPL.xlsx')


data['Smoothed'] = data['Adj Close'].rolling(window=5).mean()


bounded = []
for i in range(len(data['Adj Close'])):
    if i < 5:
        bounded.append(data['Adj Close'].iloc[i])
    else:
        min_dist = abs(data['Adj Close'].iloc[i] - min(data['Adj Close'].iloc[i-5:i]))
        max_dist = abs(data['Adj Close'].iloc[i] - max(data['Adj Close'].iloc[i-5:i]))
        if min_dist < max_dist:
            bounded.append(min(data['Adj Close'].iloc[i-5:i]))
        else:
            bounded.append(max(data['Adj Close'].iloc[i-5:i]))
data['Bounded'] = bounded


plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Adj Close'], label='Raw Data')
plt.plot(data['Date'], data['Smoothed'], label='Smoothed')
plt.plot(data['Date'], data['Bounded'], label='Bounded')
plt.xlabel('Date')  
plt.ylabel('Price')
plt.title('Apple Stock Prices')
plt.legend()
plt.grid(True)
plt.show()
