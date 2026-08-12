# Calculate the perimeter of a rectangle

try:
    n = float(input("Enter the length here.: "))
    m = float(input("Enter thr breadth here.: "))

    perimater = 2*(n+m)
    print(f" perimeter of rectangle is {perimater}")

except ValueError:
    print("enter proper length or breadth")
