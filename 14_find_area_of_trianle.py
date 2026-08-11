# Calculate the area of a Triangle with radius


import math

try:
    n = int(input("Enter the base of the triangle here.: "))
    m = int(input("Enter the height of a trianlge here.: "))

    Area = 1/2 * (n * m)
    print(f"Area of the Triangle is {Area:.2f}")

except ValueError:
    print("Enter intger number")
