import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def expense_forecasting(data):
    # Prepare data for forecasting
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data['Date'].dt.month
    data['Year'] = data['Date'].dt.year

    # Feature columns and target variable
    X = data[['Month', 'Year']]
    y = data['Amount']

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate error
    mse = mean_squared_error(y_test, predictions)
    
    # Plotting the predictions
    plt.figure(figsize=(10,6))
    plt.plot(y_test.index, y_test, label='Actual')
    plt.plot(y_test.index, predictions, label='Predicted', linestyle='--')
    plt.legend()
    plt.title('Expense Forecasting')
    plt.xlabel('Date')
    plt.ylabel('Expense Amount')
    plt.show()

    return model, mse
