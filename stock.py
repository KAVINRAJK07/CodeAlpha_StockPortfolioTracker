# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 155,
    "META": 300
}

portfolio = {}
total_value = 0

print("📊 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found! Try again.")
        continue

    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total investment
print("\n------ Portfolio Summary ------")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock} -> {qty} shares × Rs.{stock_prices[stock]} = Rs.{value}")

print("\n💰 Total Investment Value =", total_value)

# Optionally save to file
save = input("Do you want to save the result to a file? (yes/no): ")

if save.lower() == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            file.write(f"{stock} -> {qty} shares = Rs.{value}\n")
        file.write("\nTotal Investment: Rs." + str(total_value))

    print("📁 Portfolio saved as 'portfolio_summary.txt'")
