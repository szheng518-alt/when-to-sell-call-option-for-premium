import requests
import pandas as pd
import numpy as np

# Function to fetch Bitcoin price data from CoinGecko API

def fetch_bitcoin_data():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30'
    response = requests.get(url)
    data = response.json()
    prices = data['prices']
    bitcoin_data = pd.DataFrame(prices, columns=['timestamp', 'price'])
    # Convert timestamp to readable date
    bitcoin_data['date'] = pd.to_datetime(bitcoin_data['timestamp'], unit='ms')
    bitcoin_data.set_index('date', inplace=True)
    return bitcoin_data['price']

# Function to apply Elliott Wave Theory analysis for forecasting

def elliott_wave_forecast(prices):
    # Simple implementation for demonstration purposes
    # In reality, this would require more complex calculations and patterns
    # Here we will just simulate it by returning the moving average and an example of projection

    # Calculate moving average
    moving_average = prices.rolling(window=5).mean()  
    # Simple forecast: Predict next week's price based on average
    forecasted_price = moving_average.iloc[-1] * 1.05  # Assume a 5% increase for simplicity
    return forecasted_price

# Main execution flow
if __name__ == '__main__':
    btc_prices = fetch_bitcoin_data()
    forecasted_price = elliott_wave_forecast(btc_prices)
    print(f'Forecasted Bitcoin Price for next week: ${forecasted_price:.2f}')