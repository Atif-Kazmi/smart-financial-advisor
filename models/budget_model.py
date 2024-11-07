from models.budget_model import BudgetModel

# Sample data
income = 3000
expenses = {
    'Rent': 1200,
    'Groceries': 400,
    'Utilities': 150,
    'Transportation': 100,
    'Entertainment': 200
}

# Create a BudgetModel instance
budget = BudgetModel(income, expenses)

# Get insights and breakdown
print(budget.calculate_budget_balance())  # Remaining balance
print(budget.budget_insights())           # Budget insights and advice
print(budget.display_expense_breakdown())  # Expense breakdown by category
