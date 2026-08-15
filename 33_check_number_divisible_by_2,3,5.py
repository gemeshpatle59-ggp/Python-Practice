# Check whether a number is divisible by 2, 3, and 5

try:
    n = int(input('Enter the number here.: '))

    num = [2,3,5]

    for i in num:
        if n % i == 0:
            print(f"The number is divisible by {i}")

        else:
            print("The number is not divisible by any of 2,3 and 5")    

except ValueError:
    print("please enter the valid number in input.")                  