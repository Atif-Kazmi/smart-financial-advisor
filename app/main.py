import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Dynamically add the 'models' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

# Debugging: Check the sys.path to see if models folder is included
st.write(f"Current sys.path: {sys.path}")

# Try to import the BudgetModel class after appending the path
try:
    from budget_model import BudgetModel  # Absolute import from 'models' directory
    from savings_model import SavingsModel  # Import SavingsModel if needed
    from expense_forecasting import ExpenseForecasting  # Import ExpenseForecasting model
    from savings_strategies import SavingsStrategies  # Import SavingsStrategies model
except ImportError as e:
    st.error(f"Error importing models: {e}")

# Function to load expenses data
def load_expenses_data(file):
    try:
        # Attempt to load the CSV file
        data = pd.read_csv(file)
        return data
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

# Function to generate charts for expense data
def plot_expense_breakdown(expenses):
    expense_df = pd.DataFrame(expenses.items(), columns=['Category', 'Amount'])
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Amount', data=expense_df, palette='Blues_d')
    plt.xticks(rotation=45)
    plt.title('Expense Breakdown')
    st.pyplot(plt)

# Main function for Streamlit app
def main():
    # Display the app's header
    st.title("Smart Financial Advisor")
    st.write("This app helps you manage your monthly budget and predict future expenses.")

    # Sidebar for file upload and manual inputs
    st.sidebar.header("Expense Tracker")

    # Allow users to upload their expense data file
    uploaded_file = st.sidebar.file_uploader("Upload your monthly expense CSV", type="csv")
    
    if uploaded_file:
        # Load the uploaded expense data
        expense_data = load_expenses_data(uploaded_file)
        if expense_data is not None:
            st.write("### Your Uploaded Expense Data:")
            st.write(expense_data)

            # Allow users to input their income
            income = st.sidebar.number_input("Enter your monthly income:", min_value=1000, step=1000)

            if income > 0:
                # Create a BudgetModel instance
                expenses = expense_data.set_index('Category')['Amount'].to_dict()
                budget = BudgetModel(income, expenses)

                # Show budget insights
                st.write("### Budget Overview")
                st.write("**Remaining Balance:**", budget.calculate_budget_balance())
                st.write("**Budget Insights:**", budget.budget_insights())

                # Display the expense breakdown
                st.write("### Expense Breakdown")
                st.write(budget.display_expense_breakdown())
                plot_expense_breakdown(expenses)

                # Predictions for future expenses
                st.write("### Predicted Expenses for Next Month")
                predicted_expenses = {category: amount * 1.1 for category, amount in expenses.items()}  # Simple prediction (10% increase)
                st.write(predicted_expenses)
                plot_expense_breakdown(predicted_expenses)

                # Optional: Provide savings goal recommendations using the savings_model.py
                savings_model = SavingsModel(income, expenses)
                st.write("### Suggested Savings Strategies")
                st.write(savings_model.calculate_savings_goal())
                st.write(savings_model.savings_advice())

    else:
        st.write("Please upload your expense data to proceed.")

if __name__ == "__main__":
    main()
