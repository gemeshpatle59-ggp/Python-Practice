# Check whether a number is divisible by 5 and 11


try:

    n = float(input("Enter the number here.: "))

    if n % 5 == 0 :
        print(f"the number {n} is dividible by 5")

    elif n % 11 == 0:
        print(f"the number {n} is divisible by 11")    

    else:
        print("the number is not divisible by 5 or 11")
        
except ValueError:
    print("Enter number porperly..")    
