# models/savings_strategies.py

def suggest_savings_strategies(savings_goal, discretionary_income):
    strategies = []
    if discretionary_income < savings_goal:
        strategies.append("Reduce discretionary spending.")
    else:
        strategies.append("Increase savings for a higher goal.")
    return strategies
