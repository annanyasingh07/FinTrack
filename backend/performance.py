"""
FinTrack - Investment Performance Analysis

Compares the investment returns of simulated stocks.
"""

import matplotlib.pyplot as plt
from main import portfolio, calculate_stock
from pathlib import Path


def create_performance_chart(stocks):
    symbols = []
    returns = []

    for stock in stocks:
        result = calculate_stock(stock)
        symbols.append(result["symbol"])
        returns.append(result["return_percent"])

    plt.figure(figsize=(9, 6))

    bars = plt.bar(
        symbols,
        returns,
        color=["steelblue", "orange", "green"]
    )

    plt.title("FinTrack - Stock Investment Returns")
    plt.xlabel("Stock Symbol")
    plt.ylabel("Investment Return (%)")
    plt.axhline(0, color="black", linewidth=0.8)

    for bar, value in zip(bars, returns):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:.2f}%",
            ha="center",
            va="bottom" if value >= 0 else "top"
        )

    plt.tight_layout()

    output_dir = Path(__file__).resolve().parent.parent / "docs"
    output_dir.mkdir(exist_ok=True)

    plt.savefig(output_dir / "investment_performance.png")
    print("Investment performance chart saved successfully!")

    plt.show()


if __name__ == "__main__":
    create_performance_chart(portfolio)
