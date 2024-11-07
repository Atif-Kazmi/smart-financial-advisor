class BudgetModel:
    def __init__(self, income, expenses):
        """
        Initializes the BudgetModel with income and expenses data.

        :param income: The total monthly income.
        :param expenses: A dictionary of expense categories and their amounts.
        """
        self.income = income
        self.expenses = expenses

    def calculate_budget_balance(self):
        """
        Calculates the remaining balance after expenses are subtracted from income.

        :return: Remaining balance
        """
        total_expenses = sum(self.expenses.values())
        remaining_balance = self.income - total_expenses
        return remaining_balance

    def budget_insights(self):
        """
        Provides insights and advice based on the current budget.

        :return: A string containing budget insights and advice
        """
        total_expenses = sum(self.expenses.values())
        savings_potential = self.income - total_expenses

        # Basic insights
        insights = []
        if savings_potential > 0:
            insights.append("You have a positive savings potential!")
        elif savings_potential < 0:
            insights.append("You're spending more than your income. Consider cutting back on discretionary expenses.")
        else:
            insights.append("Your budget is balanced, but there's no room for additional savings.")

        # Expense advice
        high_expense_categories = [category for category, amount in self.expenses.items() if amount > 0.2 * self.income]
        if high_expense_categories:
            insights.append(f"High spending categories: {', '.join(high_expense_categories)}. Consider reviewing these.")

        return " ".join(insights)

    def display_expense_breakdown(self):
        """
        Displays a detailed breakdown of the expenses by category.

        :return: A string containing the expense breakdown by category
        """
        breakdown = "\n".join([f"{category}: ${amount}" for category, amount in self.expenses.items()])
        return breakdown


# Example usage:
if __name__ == "__main__":
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
    print("Remaining balance:", budget.calculate_budget_balance())  # Remaining balance
    print("Budget Insights:", budget.budget_insights())           # Budget insights and advice
    print("Expense Breakdown:\n", budget.display_expense_breakdown())  # Expense breakdown by category
