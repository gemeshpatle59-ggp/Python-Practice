# Convert Celsius to Fahrenheit

try:
    n = float(input("Enter the Celsius here.: "))

    fahrenheit = (n * 9/5) + 32
    print(f"{n}° celsius is {fahrenheit:.1f}° fahrenheit ")

except ValueError:
    print("enter proper length or breadth")
