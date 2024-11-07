from models.budget_model import BudgetModel
import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Title and Introduction
st.title("Smart Financial Advisor")
st.header("Budgeting & Savings Tracker")

# Input Section
st.sidebar.header("User Inputs")
income = st.sidebar.number_input("Enter your monthly income:", min_value=1000, max_value=100000, value=3000, step=500)

# Expense Categories: Allow users to add categories dynamically
expense_categories = ['Rent', 'Groceries', 'Utilities', 'Transportation', 'Entertainment', 'Other']
expenses = {}
for category in expense_categories:
    amount = st.sidebar.number_input(f"Enter your {category} expenses:", min_value=0, max_value=10000, value=300, step=50)
    expenses[category] = amount

# Create BudgetModel instance
budget = BudgetModel(income, expenses)

# Section for Budget Insights
st.subheader("Budget Insights")
remaining_balance = budget.calculate_budget_balance()
st.write(f"Remaining Balance: ${remaining_balance}")
insights = budget.budget_insights()
st.write(insights)

# Expense Breakdown Section
st.subheader("Expense Breakdown")
expense_details = budget.display_expense_breakdown()
st.text(expense_details)

# Expense Visualization
st.subheader("Expense Allocation")
fig, ax = plt.subplots(figsize=(10, 6))
categories = list(expenses.keys())
amounts = list(expenses.values())
ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Savings Goal Tracker
st.subheader("Savings Goal Tracker")
goal = st.number_input("Enter your savings goal:", min_value=100, max_value=50000, value=5000, step=500)
savings_progress = (income - sum(expenses.values())) / income * 100  # Simple savings progress
st.write(f"Current Savings Progress: {savings_progress:.2f}%")

# Visualize savings progress
fig, ax = plt.subplots(figsize=(6, 4))
ax.barh(['Savings Progress'], [savings_progress], color='green')
ax.set_xlim(0, 100)
ax.set_xlabel("Savings Progress (%)")
st.pyplot(fig)

# File Upload for Monthly Expense Sheet
st.subheader("Upload Your Monthly Expense Sheet (CSV)")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Show the uploaded data
    st.write("Uploaded Expense Data:")
    st.dataframe(df.head())
    
    # Process the data (ensure the columns are correct)
    if 'Category' in df.columns and 'Amount' in df.columns:
        # Convert Amount column to numeric
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')  # Convert to numeric
        df = df.dropna()  # Drop rows with NaN values
        
        # Group by 'Category' and get the sum for each category
        category_expenses = df.groupby('Category')['Amount'].sum().reset_index()

        # Check if there are enough records to predict
        if len(category_expenses) < 2:
            st.error("Insufficient data to make a prediction.")
        else:
            # Prepare the data for Linear Regression
            X = np.array(range(len(category_expenses))).reshape(-1, 1)  # Month number (0, 1, 2, 3,...)
            y = category_expenses['Amount'].values  # Expenses for each category

            # Initialize and fit the model
            model = LinearRegression()
            model.fit(X, y)
            
            # Predict next month's expenses (i.e., the next point in the trend)
            next_month_prediction = model.predict(np.array([[len(category_expenses)]]))
            
            # Display predicted expenses for next month
            predicted_expenses = pd.DataFrame({
                'Category': category_expenses['Category'],
                'Predicted Expense for Next Month': next_month_prediction
            })
            
            st.subheader("Predicted Expenses for Next Month")
            st.write(predicted_expenses)

            # Visualize predicted expenses
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(predicted_expenses['Category'], predicted_expenses['Predicted Expense for Next Month'], color='orange')
            ax.set_xlabel('Expense Category')
            ax.set_ylabel('Predicted Expense ($)')
            st.pyplot(fig)
    else:
        st.error("The CSV file must contain 'Category' and 'Amount' columns.")
