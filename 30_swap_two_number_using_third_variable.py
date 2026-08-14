# Swap two numbers using a third variable                               

try: 
    n = int(input("Enter the first number here.: "))
    m = int(input("Enter the second number here.: "))

    temp = n

    n = m
    m = temp

    print(f"the swaped valuse is")
    print(f"n = {n}")
    print(f"m = {m}")

except ValueError:
    print("please enter the peoper number in input.")    