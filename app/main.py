import sys
import os
import streamlit as st

# Step 1: Add the parent directory (the root of the project) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Step 2: Try importing BudgetModel from the models directory
try:
    from models.budget_model import BudgetModel
    st.write("BudgetModel imported successfully.")
except ModuleNotFoundError as e:
    st.write(f"Error: {e}")

# Step 3: Streamlit UI

# Title of the app
st.title("Smart Financial Advisor")

# Instructions or welcome message
st.write("Welcome to the Smart Financial Advisor app! This tool helps you manage your finances, track your budget, and save money effectively.")

# Check if the model is imported successfully
if 'BudgetModel' in locals():
    # If the model is successfully imported, instantiate and use it
    budget_model = BudgetModel()

    # Example interaction with the model
    st.write("The BudgetModel has been successfully imported and is now available for use.")

    # Sample method or interaction with the BudgetModel (Example)
    if st.button('Run Budget Analysis'):
        # Here you would call methods from the BudgetModel class to interact with it
        # For example, assuming BudgetModel has a method like 'get_budget_analysis'
        budget_data = budget_model.get_budget_analysis()  # Replace with actual method
        st.write("Budget Analysis Results:", budget_data)

else:
    # In case the import fails, show an error message
    st.write("Error: Could not import the BudgetModel. Please check the directory structure or the code.")
