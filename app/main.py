from scripts.data_visualization import income_vs_expenses
from scripts.savings_progress import savings_progress

# Visualize Income vs Expenses
if st.button("Income vs Expenses"):
    income_vs_expenses(income, expenses_df)

# Visualize Savings Progress
if st.button("Savings Progress"):
    savings_progress(income, expenses_df)
