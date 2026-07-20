import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# 1. Generate synthetic time series data (Monthly Sales over 5 years)
np.random.seed(42)
months = pd.date_range(start='2018-01-01', periods=60, freq='ME')
month_numbers = np.array(months, dtype=float)
# ✅ FIX: Extract month numbers cleanly

trend = np.linspace(100, 200, 60)
seasonality = 10 * np.sin(2 * np.pi * month_numbers / 12)
noise = np.random.normal(loc=0, scale=5, size=60)
sales = trend + seasonality + noise

# 2. Create DataFrame
df = pd.DataFrame({'Date': months, 'Sales': sales})
df.set_index('Date', inplace=True)

# 3. Train/Test Split
train = df.iloc[:-12]
test = df.iloc[-12:]

train.index.freq = 'ME'
rest.index.freq = 'ME'

# 4. Holt-Winters Model (Triple Exponential Smoothing)
model = ExponentialSmoothing(train['Sales'],
                             trend='add',
                             seasonal='add',
                             seasonal_periods=12)
fit = model.fit()

# 5. Forecast next 12 months
forecast = fit.forecast(12)

# 6. Calculate MAE
mae = mean_absolute_error(test['Sales'], forecast)
print(f"Mean Absolute Error: {mae:.2f}")

# 7. Plot the results
plt.figure(figsize=(12, 6))
plt.plot(train.index, train['Sales'], label='Training Data', color='blue')
plt.plot(test.index, test['Sales'], label='Actual Sales', color='green')
plt.plot(test.index, forecast, label='Forecasted Sales', color='red', linestyle='--')
plt.title('Monthly Sales Forecast using Holt-Winters Method', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
