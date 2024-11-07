import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from models.budget_model import BudgetModel
import sys
# Function to load expenses data
def load_expenses_data(file):
    try:
        data = pd.read_csv(file)
        return data
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

# Function to generate charts for expense data
def plot_expense_breakdown(expenses):
    # Plotting a bar chart
    expense_df = pd.DataFrame(expenses.items(), columns=['Category', 'Amount'])
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Amount', data=expense_df, palette='Blues_d')
    plt.xticks(rotation=45)
    plt.title('Expense Breakdown')
    st.pyplot(plt)

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
                # Implement a simple prediction based on last month's expense data (e.g., increase by 10%)
                predicted_expenses = {category: amount * 1.1 for category, amount in expenses.items()}
                st.write(predicted_expenses)
                plot_expense_breakdown(predicted_expenses)

    else:
        st.write("Please upload your expense data to proceed.")

if __name__ == "__main__":
    main()
