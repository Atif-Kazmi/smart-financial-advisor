import streamlit as st
import pandas as pd
import sys

# Add the models folder to the Python path
sys.path.append('./models')  # This ensures the 'models' directory can be accessed

# Import BudgetModel from the 'models' folder
from budget_model import BudgetModel

# File path to the CSV file in the main directory
csv_file_path = 'expenses_data.csv'

# Function to load the expense data from CSV file
def load_expenses_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        st.error(f"Error loading the file: {e}")
        return None

# Load the expense data from the CSV file
expense_data = load_expenses_data(csv_file_path)

# If data is loaded, proceed with calculations
if expense_data is not None:
    # Assuming the CSV has columns 'Category' and 'Amount'
    expenses = expense_data.set_index('Category')['Amount'].to_dict()

    # Allow user to input their monthly income
    income = st.number_input("Enter your monthly income:", min_value=1000, step=1000)

    if income > 0:
        # Create an instance of BudgetModel
        budget = BudgetModel(income, expenses)
        
        # Display the results
        st.write("### Budget Overview")
        st.write("**Remaining Balance:**", budget.calculate_budget_balance())
        st.write("**Budget Insights:**", budget.budget_insights())
        st.write("**Expense Breakdown:**", budget.display_expense_breakdown())
else:
    st.error("No expense data available.")
