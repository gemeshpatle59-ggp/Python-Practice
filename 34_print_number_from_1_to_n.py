# Print numbers from 1 to N

try:
    n = int(input("Enter the number here.: "))

    def num(n):
        if n == 0:
            return 
        num(n-1)
        print(n)

    num(n)    

except ValueError:
    print("Please enter the valid number in input.")



