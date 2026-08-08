try:
    n = float(input("Enter the number here.: "))

    if n < 0:
        print(f""
              f"{n} is a negative number."
              )

    elif n > 0:
        print(f""
              f"{n} is a positive number."
              )

    else :
        print(f""
              f"{n} is zero.."
              )    
except ValueError:
    print("check the number ")    

