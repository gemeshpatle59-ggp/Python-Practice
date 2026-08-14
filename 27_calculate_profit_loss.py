# Calculate profit or loss 

def Calculate_profit_loss(selling_price,cost_price):
    if selling_price > cost_price:
        print("The profit is of rs.",selling_price - cost_price)
    elif selling_price == cost_price:
        print("No loss no profit")
    else:
        print("The loss is of rs.",cost_price - selling_price)      

try:
    n = int(input("Enter the selling price here.: "))          
    m = int(input("Enter the costprice here.: "))

    Calculate_profit_loss(n,m)

except ValueError:
    print("print the valid number of prices.")
