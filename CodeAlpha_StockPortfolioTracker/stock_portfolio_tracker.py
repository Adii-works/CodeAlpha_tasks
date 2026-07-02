def stock_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGLE": 140,
        "MSFT": 320
    }

    total = 0

    print("Available Stocks:")
    for stock in stock_prices:
        print(stock)

    while True:
        stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

        if stock_name == "DONE":
            break

        if stock_name in stock_prices:
            quantity = int(input("Enter quantity: "))
            investment = stock_prices[stock_name] * quantity
            total += investment
            print("Investment:", investment)
        else:
            print("Stock not found.")

    print("\nTotal Investment =", total)


stock_tracker()