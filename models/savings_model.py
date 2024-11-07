# models/savings_model.py

class SavingsModel:
    def __init__(self, income, savings_goal):
        self.income = income
        self.savings_goal = savings_goal

    def calculate_savings_goal(self):
        return self.savings_goal / self.income
