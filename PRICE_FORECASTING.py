import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

ticker = "AAPL"       # Change to INFY, TATASTEEL, RELIANCE, NIFTY50
data = yf.download(ticker, start="2015-01-01", end="2025-01-01")
df = data["Close"]
df.plot()

train_size = int(len(df) * .55)
train, test = df[:train_size], df[train_size:]

model = ARIMA(train, order=(5,1,0))  # Example
model_fit = model.fit()
print(model_fit.summary())

forecast = model_fit.forecast(steps=len(test))

plt.plot(test.index, test, label="Actual")
plt.plot(test.index, forecast, label="Predicted")
plt.legend()
plt.show()

rmse = np.sqrt(mean_squared_error(test, forecast))
print("RMSE:", rmse)
