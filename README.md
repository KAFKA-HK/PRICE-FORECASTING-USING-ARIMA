# PRICE-FORECASTING-USING-ARIMA

📈 Stock Price Forecasting using ARIMA (Time Series Analysis)
📌 Overview

This project demonstrates time series forecasting of stock prices using the ARIMA (AutoRegressive Integrated Moving Average) model.
Historical stock data is fetched directly from Yahoo Finance using the yfinance library, and future prices are predicted based on past trends.

The project provides a simple yet strong introduction to classical time series modeling, commonly used in quant finance and financial analytics.

🚀 Features

Fetches real-world stock market data automatically

Uses ARIMA for time series forecasting

Train–test split on chronological data

Visual comparison of actual vs predicted prices

Model evaluation using RMSE

Easily configurable for different stocks or indices

🧠 Problem Statement

Financial time series data is:

Sequential

Trend-based

Non-stationary

This project aims to model historical closing prices and forecast future values using statistical time series techniques.

🛠️ Tech Stack

Python

Pandas, NumPy

yFinance

Matplotlib

Statsmodels

Scikit-learn

📂 Project Structure
stock-price-forecasting-arima/
│
├── arima_forecast.py        # Main script
├── requirements.txt         # Dependencies
├── README.md                # Documentation
└── .gitignore

📊 Dataset

Source: Yahoo Finance

Data Type: Historical stock prices

Feature Used: Close price

Date Range: 2015-01-01 to 2025-01-01

You can change the ticker symbol:

ticker = "AAPL"  # Examples: INFY, TATASTEEL, RELIANCE, ^NSEI

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/stock-price-forecasting-arima.git
cd stock-price-forecasting-arima

2️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run
python arima_forecast.py

🔄 Methodology
1. Data Collection

Historical stock prices downloaded using yfinance

2. Data Preparation

Extracted closing prices

Chronological train-test split (55% train, 45% test)

3. Model Training
ARIMA(order=(5,1,0))


AR (5): Autoregressive terms

I (1): Differencing for stationarity

MA (0): Moving average terms

4. Forecasting

Forecasted prices for the test period

5. Evaluation

Root Mean Squared Error (RMSE)

📈 Output & Visualization

Line plot of historical prices

Actual vs Predicted price comparison

RMSE score printed in console

Example:

RMSE: 4.21

📉 Limitations

ARIMA assumes linear relationships

Does not capture sudden market shocks

Sensitive to parameter selection

🔮 Future Improvements

Auto ARIMA for parameter tuning

SARIMA for seasonality

Compare with LSTM / Prophet

Rolling window forecasting

Hyperparameter optimization

🎓 What I Learned

Time series fundamentals

Stationarity and differencing

ARIMA modeling workflow

Financial data analysis

Forecast evaluation techniques

👨‍💻 Author

Harikrishnan SG
Aspiring AI / ML Engineer
Interested in Quantitative Finance, Time Series, and ML Systems

⭐ Acknowledgements

Yahoo Finance

Statsmodels

Scikit-learn

Python Open Source Community
