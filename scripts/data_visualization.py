# scripts/data_visualization.py

import matplotlib.pyplot as plt

def visualize_data(expenses):
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.title("Expense Breakdown")
    plt.xlabel("Categories")
    plt.ylabel("Amount")
    plt.show()
