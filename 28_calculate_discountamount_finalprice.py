# Calculate discount amount and final price 

try: 
    n = int(input("Enter the original price here.: "))
    m = int(input("Enter the discount percentage here .: "))

    dicount_amount = n *(m/100)

    final_price = n - dicount_amount

    print(f"the discount amount is {dicount_amount} and final price is {final_price}")    

except ValueError:
    print("please enter the valid  number in price or discount.")    