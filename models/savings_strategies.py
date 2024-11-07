def suggest_savings_strategy(income, expenses_df):
    total_expenses = expenses_df['Amount'].sum()
    savings = income - total_expenses
    
    if savings > income * 0.20:
        strategy = "High Savings: Consider investing in high-return assets."
    elif savings > income * 0.10:
        strategy = "Moderate Savings: Look into medium-risk investment options."
    else:
        strategy = "Low Savings: Prioritize reducing non-essential expenses."
    
    return strategy
