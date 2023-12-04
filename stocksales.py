# Troy Jeffrey Amegashie
# Stock Sales
# 03/24/2020

from stackqueue import Stack
from stackqueue import Queue

method = 0

while method != 3:
    print("This platform helps you keep track of your stock portfolio and report your profits. What accounting method would you like to proceed with?")
    print("1. LIFO")
    print("2. FIFO")
    print("3. Exit Program")
    method = int(input(">"))

    if method == 1:
        total_stocks = 0
        total_profit = 0.0
        total_value_bought = 0.0
        total_value_sold = 0.0
        stock_qty = Stack()
        stock_price = Stack()
        stock_names = []
        choice = 0

        while choice != 5:
            print("Please select an option from the menu below:")
            print("1. Buy stocks (Long)")
            print("2. Sell stocks (Short) ")
            print("3. View current portfolio")
            print("4. View Profit/Loss")
            print("5. Exit Program")
            choice = int(input(">"))

            if choice == 1:
                name = input("What company stock would like to buy? (Ex. Amazon, Apple)\n >")
                qty = int(input("How many shares would you like to buy?"))
                price = float(input("What's the market price for each stock?"))
                stock_names.append(name)
                stock_qty.push(qty)
                stock_price.push(price)
                stock_value = qty * price
                total_value_bought += stock_value
                print(f"{qty} {name} stocks Added to Portfolio. \n\n")
                total_stocks += qty

            elif choice == 2:
                name = input("What company stock would you like to sell?\n >")
                qty_needed = int(input("How many shares are you looking to sell?"))
                if qty_needed > total_stocks:
                    print(f"You do not have {qty_needed} stocks available for sale.\n\n")
                    continue
                else:
                    total_popped = 0
                    total_sale = 0.0
                    qty_popped = stock_qty.pop()
                    total_stocks -= qty_popped
                    price = stock_price.pop()
                    total_sale += (qty_popped * price)
                    total_popped += qty_popped
                    while total_popped < qty_needed:
                        qty_popped = stock_qty.pop()
                        total_stocks -= qty_popped
                        price = stock_price.pop()
                        total_sale += (qty_popped * price)
                        total_popped += qty_popped
                    if total_popped > qty_needed:
                        overage = total_popped - qty_needed
                        stock_qty.push(overage)
                        stock_price.push(price)
                        total_stocks += overage
                        total_sale -=(overage * price)
                        # Profit/Loss
                        total_value_sold += total_sale
                        profit_loss = total_value_bought - total_value_sold
                        total_profit = profit_loss
                print(f"You have successfully filled the order for {qty_needed} shares\n")

            elif choice == 3:

                print(f"You currently hold shares in the following companies:\n {stock_names}")
                print(f"You currently have a total of {total_stocks} shares \n")

            elif choice == 4:
                print(f"Your Realized Profit/Loss is ${total_profit}\n")

    elif method == 2:
        total_stocks = 0
        total_profit = 0.0
        total_value_bought = 0.0
        total_value_sold = 0.0
        stock_qty = Queue()
        stock_price = Queue()
        stock_names = []
        choice = 0

        while choice != 5:
            print("Please select an option from the menu below:")
            print("1. Buy stocks (Long)")
            print("2. Sell stocks (Short) ")
            print("3. View current portfolio")
            print("4. View Profit/Loss")
            print("5. Exit Program")
            choice = int(input(">"))

            if choice == 1:
                name = input("What company stock would like to buy? (Ex. Amazon, Apple)\n >")
                qty = int(input("How many shares would you like to buy?"))
                price = float(input("What's the market price for each stock?"))
                stock_names.append(name)
                stock_qty.push(qty)
                stock_price.push(price)
                stock_value = qty * price
                total_value_bought += stock_value
                print("Added to inventory. \n\n")
                total_stocks += qty

            elif choice == 2:
                name = input("What company stock would you like to sell?\n >")
                qty_needed = int(input("How many shares are you looking to sell?"))
                if qty_needed > total_stocks:
                    print(f"You do not have {qty_needed} stocks available for sale.\n\n")
                    continue
                else:
                    total_popped = 0
                    total_sale = 0.0
                    qty_popped = stock_qty.pop()
                    total_stocks -= qty_popped
                    price = stock_price.pop()
                    total_sale += (qty_popped * price)
                    total_popped += qty_popped
                    while total_popped < qty_needed:
                        qty_popped = stock_qty.pop()
                        total_stocks -= qty_popped
                        price = stock_price.pop()
                        total_sale += (qty_popped * price)
                        total_popped += qty_popped
                    if total_popped > qty_needed:
                        overage = total_popped - qty_needed
                        stock_qty.push(overage)
                        stock_price.push(price)
                        total_stocks += overage
                        total_sale -= (overage * price)
                        # Profit/Loss
                        total_value_sold += total_sale
                        profit_loss = total_value_bought - total_value_sold
                        total_profit = profit_loss
                print(f"You have successfully filled the order for {qty_needed} shares\n")

            elif choice == 3:

                print(f"You currently hold shares in the following companies:\n {stock_names}")
                print(f"You currently have a total of {total_stocks} shares \n")

            elif choice == 4:
                print(f"Your Realized Profit/Loss is ${total_profit}\n")
