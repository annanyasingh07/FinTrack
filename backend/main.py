"""
FinTrack - Investment Analytics Platform
Step 2: Stock Portfolio Calculator

This program analyzes a hypothetical stock portfolio.
All stock prices are sample data, not live market prices.
"""

# Step 1: Define our sample portfolio
portfolio = [
    {
        "symbol": "AAPL",
        "shares": 10,
        "purchase_price": 150.00,
        "current_price": 180.00
    },
    {
        "symbol": "MSFT",
        "shares": 5,
        "purchase_price": 300.00,
        "current_price": 350.00
    },
    {
        "symbol": "NVDA",
        "shares": 8,
        "purchase_price": 100.00,
        "current_price": 120.00
    }
]


# Step 2: Calculate individual stock performance
def calculate_stock(stock):
    initial_value = stock["shares"] * stock["purchase_price"]
    current_value = stock["shares"] * stock["current_price"]

    profit_loss = current_value - initial_value
    return_percent = (profit_loss / initial_value) * 100

    return {
        "symbol": stock["symbol"],
        "initial_value": initial_value,
        "current_value": current_value,
        "profit_loss": profit_loss,
        "return_percent": return_percent
    }


# Step 3: Calculate overall portfolio performance
def calculate_portfolio(stocks):
    total_investment = 0
    total_value = 0

    print("\nFINTRACK - PORTFOLIO SUMMARY")
    print("-" * 45)

    for stock in stocks:
        result = calculate_stock(stock)

        total_investment += result["initial_value"]
        total_value += result["current_value"]

        print(f"Stock: {result['symbol']}")
        print(f"Initial Value: ${result['initial_value']:.2f}")
        print(f"Current Value: ${result['current_value']:.2f}")
        print(f"Profit/Loss: ${result['profit_loss']:.2f}")
        print(f"Return: {result['return_percent']:.2f}%")
        print("-" * 45)

    total_profit = total_value - total_investment
    total_return = (total_profit / total_investment) * 100

    print("\nTOTAL PORTFOLIO PERFORMANCE")
    print(f"Total Investment: ${total_investment:.2f}")
    print(f"Current Value: ${total_value:.2f}")
    print(f"Total Profit/Loss: ${total_profit:.2f}")
    print(f"Total Return: {total_return:.2f}%")


# Step 4: Run the program
if __name__ == "__main__":
    calculate_portfolio(portfolio)

# Step 5: Analyze portfolio allocation
def calculate_allocation(stocks):
    total_value = sum(
        stock["shares"] * stock["current_price"]
        for stock in stocks
    )

    print("\nFINTRACK - PORTFOLIO ALLOCATION")
    print("-" * 45)

    for stock in stocks:
        stock_value = stock["shares"] * stock["current_price"]
        allocation = (stock_value / total_value) * 100

        print(f"Stock: {stock['symbol']}")
        print(f"Current Value: ${stock_value:.2f}")
        print(f"Portfolio Allocation: {allocation:.2f}%")
        print("-" * 45)


# Run portfolio allocation analysis
if __name__ == "__main__":
    calculate_allocation(portfolio)
