# models/budget_model.py

class BudgetModel:
    def __init__(self, income, expenses, savings_goal):
        self.income = income
        self.expenses = expenses
        self.savings_goal = savings_goal

    def calculate_total_expenses(self):
        return sum(self.expenses.values())

    def calculate_budget_allocation(self):
        total_expenses = self.calculate_total_expenses()
        discretionary_income = self.income - total_expenses - self.savings_goal
        allocation = {
            "income": self.income,
            "total_expenses": total_expenses,
            "savings_goal": self.savings_goal,
            "discretionary_income": max(discretionary_income, 0)
        }
        return allocation
