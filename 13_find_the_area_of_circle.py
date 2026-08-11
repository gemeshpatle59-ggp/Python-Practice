# Calculate the area of a circle with radius


import math
try:
    n = int(input("Enter the radius of circle here.: "))

    Area = math.pi * (n**2)
    print(f"Area of the circle is {Area:.2f}")

except ValueError:
    print("Enter intger number")
