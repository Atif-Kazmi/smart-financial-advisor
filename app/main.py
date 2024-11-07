# app/main.py
import sys
import os

import streamlit as st
from models.budget_model import BudgetModel
from models.savings_model import SavingsModel
from scripts.expense_tracker import ExpenseTracker
from scripts.goal_tracker import GoalTracker
from scripts.data_visualization import visualize_data
from scripts.savings_progress import show_savings_progress

st.title("Smart Financial Advisor")

# Sample user input
income = st.number_input("Enter your monthly income:", min_value=0)
savings_goal = st.number_input("Enter your monthly savings goal:", min_value=0)
expenses = {
    "rent": st.number_input("Rent:", min_value=0),
    "food": st.number_input("Food:", min_value=0),
    "utilities": st.number_input("Utilities:", min_value=0),
    "transportation": st.number_input("Transportation:", min_value=0),
    "entertainment": st.number_input("Entertainment:", min_value=0),
}

# Budget Model
budget = BudgetModel(income, expenses, savings_goal)
allocation = budget.calculate_budget_allocation()
st.write("Budget Allocation:", allocation)

# Expense Tracking
tracker = ExpenseTracker(expenses)
tracker.update_expenses()
st.write("Updated Expenses:", tracker.expenses)

# Savings Goal
savings_model = SavingsModel(income, savings_goal)
goal = savings_model.calculate_savings_goal()
st.write("Savings Goal:", goal)

# Data Visualization
visualize_data(tracker.expenses)

# Show Savings Progress
show_savings_progress(goal)
