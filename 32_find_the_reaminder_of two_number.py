# Find the remainder of two numbers

try:
    n ,m = map(int,input("Enter the 1st number here.: ").split())
    
    remainder = (n %  m)

    print(f"\nThe remainder of two number is { remainder}")

except ValueError:
    print("Please enter the vaild number in input.")    