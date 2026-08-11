# Calculate the cube of a number


try:
    n = int(input("Enter the number here.: "))

    cube = n ** 3
    print(f"cube of {n} is {cube}")

except ValueError:
    print("Enter intger number")
