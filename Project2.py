cost_price = int(input("Enter the Cost Price (CP): "))
selling_price = int(input("Enter the Selling Price (SP): "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"You made a profit of ₹{profit}.")
if selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"You incurred a loss of ₹{loss}.")
if selling_price == cost_price:
    print("No profit, no loss. You broke even!")