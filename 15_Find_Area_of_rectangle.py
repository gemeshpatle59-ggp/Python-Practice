# Calculate the area of a rectangle

try:
    n = float(input("Enter the length here.: "))
    m = float(input("Enter thr breadth here.: "))

    area = (n*m)
    print(f"area of rectangle is {area}")

except ValueError:
    print("enter proper length or breadth")
