# Convert fahrenheit into celsius.

try:
    n = float(input("Enter the fahrenheit here.: "))

    celsius = (n - 32) *5/9
    print(f"{n}° fahrenhite is {celsius:.1f}° celsius ")

except ValueError:
    print("enter proper length or breadth")
