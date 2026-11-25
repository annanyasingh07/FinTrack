"""
FinTrack - Portfolio Concentration Visualization
"""

from pathlib import Path
import matplotlib.pyplot as plt
from main import portfolio


def create_concentration_chart(stocks):
    symbols = []
    allocations = []

    total_value = sum(
        stock["shares"] * stock["current_price"]
        for stock in stocks
    )

    if total_value <= 0:
        print("Cannot chart an empty portfolio.")
        return

    for stock in stocks:
        value = stock["shares"] * stock["current_price"]
        allocation = (value / total_value) * 100

        symbols.append(stock["symbol"])
        allocations.append(allocation)

    plt.figure(figsize=(9, 6))

    bars = plt.bar(
        symbols,
        allocations,
        color="steelblue"
    )

    plt.axhline(
        y=30,
        color="orange",
        linestyle="--",
        label="30% Reference Threshold"
    )

    plt.axhline(
        y=50,
        color="red",
        linestyle="--",
        label="50% Reference Threshold"
    )

    for bar, allocation in zip(bars, allocations):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            allocation + 1,
            f"{allocation:.2f}%",
            ha="center"
        )

    plt.title("FinTrack - Portfolio Concentration Analysis")
    plt.xlabel("Stock")
    plt.ylabel("Portfolio Allocation (%)")
    plt.ylim(0, 60)
    plt.legend()
    plt.tight_layout()

    output_dir = Path(__file__).resolve().parent.parent / "docs"
    output_dir.mkdir(exist_ok=True)

    plt.savefig(
        output_dir / "portfolio_concentration.png",
        dpi=150
    )

    print("Portfolio concentration chart saved successfully!")
    plt.show()


if __name__ == "__main__":
    create_concentration_chart(portfolio)
