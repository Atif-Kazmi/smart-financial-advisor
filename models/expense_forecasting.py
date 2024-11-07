# models/expense_forecasting.py

def forecast_expenses(current_expenses, months=12):
    forecast = {category: amount * months for category, amount in current_expenses.items()}
    return forecast
