# Calculate average of three numbers

try:
    n = int(input("Enter the 1st number here.: "))    
    m = int(input("Enter the 2nd number here.: "))
    o = int(input("Enter the 3rd number here.: "))

    Average = (n+m+o)/3

    print(f"The Average of three number is {Average:.2f}")

except ValueError:
    print("Enter the correct number ")
