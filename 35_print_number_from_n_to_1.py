# Print numbers from N to 1

try:
    n = int(input("Enter the number here.: "))

    def num(n):
        if n == 0:
            return 
        print(n)
        num(n-1)

    num(n)    

except ValueError:
    print("Please enter the valid number in input.")
