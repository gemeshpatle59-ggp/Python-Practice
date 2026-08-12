# Convert kilometers to meters

try:
    n = float(input("Enter the kilometer here.: "))

    meter = n * 1000
    print(f"{n} kilometer is {meter:.1f} meter ")

except ValueError:
    print("enter proper length or breadth")
