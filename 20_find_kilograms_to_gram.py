# Convert kilograms to grams.

try:
    n = float(input("Enter the kilogram here.: "))

    gram = n * 1000
    print(f"{n} kilogram is {gram:.1f} gram ")

except ValueError:
    print("enter proper length or breadth")
