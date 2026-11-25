"""
FinTrack - Portfolio Concentration Risk Analysis

Analyzes the concentration of simulated stock holdings.
"""

from main import portfolio


def analyze_risk(stocks):
    total_value = sum(
        stock["shares"] * stock["current_price"]
        for stock in stocks
    )

    if total_value <= 0:
        print("Cannot analyze an empty portfolio.")
        return

    print("\nFINTRACK - PORTFOLIO RISK ANALYSIS")
    print("-" * 45)

    allocations = []

    for stock in stocks:
        stock_value = stock["shares"] * stock["current_price"]
        allocation = (stock_value / total_value) * 100

        allocations.append((stock["symbol"], allocation))

        print(f"{stock['symbol']} Allocation: {allocation:.2f}%")

    largest_stock = max(allocations, key=lambda x: x[1])

    print("\nCONCENTRATION ANALYSIS")
    print(f"Largest Holding: {largest_stock[0]}")
    print(f"Largest Allocation: {largest_stock[1]:.2f}%")

    # Illustrative thresholds, not a validated risk rating
    if largest_stock[1] > 50:
        concentration = "High"
    elif largest_stock[1] > 30:
        concentration = "Moderate"
    else:
        concentration = "Low"

    print(f"Concentration Indicator: {concentration}")
    print("\nNote: This measures single-stock concentration only.")
    print("It does not measure volatility or overall market risk.")


if __name__ == "__main__":
    analyze_risk(portfolio)
