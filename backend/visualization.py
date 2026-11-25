"""
FinTrack - Portfolio Allocation Visualization

Creates a pie chart showing the percentage of total
portfolio value invested in each stock.
"""

import matplotlib.pyplot as plt
from main import portfolio


def create_allocation_chart(stocks):
    symbols = []
    values = []

    for stock in stocks:
        symbols.append(stock["symbol"])
        values.append(stock["shares"] * stock["current_price"])

    plt.figure(figsize=(8, 6))

    plt.pie(
        values,
        labels=symbols,
        autopct="%1.2f%%",
        startangle=90
    )

    plt.title("FinTrack - Portfolio Allocation")
    plt.axis("equal")

    plt.savefig("docs/portfolio_allocation.png")
    print("Portfolio allocation chart saved successfully!")

    plt.show()


if __name__ == "__main__":
    create_allocation_chart(portfolio)
