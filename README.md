# 📈 Time Series Forecasting with Holt-Winters (Python)

This project demonstrates how to build a **time series forecasting model** using the **Holt-Winters Exponential Smoothing** technique on a **synthetic monthly sales dataset**. The goal is to model and predict future values using trend and seasonality.

---

## 🔧 Features

- 📊 Generates 5 years (60 months) of synthetic monthly sales data
- 🧠 Uses Holt-Winters (Triple Exponential Smoothing) from `statsmodels`
- 📈 Forecasts the next 12 months of sales
- 📉 Calculates **Mean Absolute Error (MAE)** for evaluation
- 🖼️ Beautiful matplotlib plots for visual comparison of actual vs forecast
- 💡 No need to import or clean external datasets — data is generated automatically!

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install pandas numpy matplotlib statsmodels scikit-learn
