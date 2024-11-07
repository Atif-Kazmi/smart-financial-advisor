class BudgetModel:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def calculate_budget_balance(self):
        """Calculate the remaining balance after expenses."""
        total_expenses = sum(self.expenses.values())
        return self.income - total_expenses

    def budget_insights(self):
        """Provide insights based on the budget."""
        total_expenses = sum(self.expenses.values())
        if self.income > total_expenses:
            return "You have a positive savings potential! High spending categories: " + self.get_high_expenses()
        else:
            return "You are spending more than your income. Consider reviewing your expenses."

    def display_expense_breakdown(self):
        """Display the expenses breakdown."""
        expense_details = ""
        for category, amount in self.expenses.items():
            expense_details += f"{category}: ${amount}\n"
        return expense_details.strip()

    def get_high_expenses(self):
        """Get high expense categories."""
        high_expenses = [category for category, amount in self.expenses.items() if amount > 500]
        return ', '.join(high_expenses) if high_expenses else "None"
