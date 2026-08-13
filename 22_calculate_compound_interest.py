# Calculate compound interest

try:
    n = int(input("Enter the principle amount here.: "))    
    m = int(input("Enter the Rate of intrest here.: "))
    o = int(input("Enter the Time period here.: "))

    ci = n*(1+ m/100)**o - n

    print(f"The compond intrest is {ci:.2f}")


except ValueError:
    print("Enter the correct value")



    
