from models.budget_model import BudgetModel
import streamlit as st

# Sample data
income = 3000
expenses = {
    'Rent': 1200,
    'Groceries': 400,
    'Utilities': 150,
    'Transportation': 100,
    'Entertainment': 200
}

# Check if the model is imported successfully
if 'BudgetModel' in locals():
    # If the model is successfully imported, instantiate and use it
    budget_model = BudgetModel(income, expenses)

    # Example interaction with the model
    st.write("The BudgetModel has been successfully imported and is now ready to use.")
    st.write("Remaining Balance: ", budget_model.calculate_budget_balance())
    st.write("Budget Insights: ", budget_model.budget_insights())
    st.write("Expense Breakdown: ", budget_model.display_expense_breakdown())
else:
    st.write("Error: BudgetModel could not be imported.")
