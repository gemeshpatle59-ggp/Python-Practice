# Check whether a year is a leap year

try:
    n = int(input("Enter the year here.: "))
    
    if n % 400 == 0 or (n % 4==0 and n % 100 != 0):
        print(f"{n} is a leap year")

    else:
        print(f"{n} is not a leap year")


except ValueError:
    print("check the year properly..")    
