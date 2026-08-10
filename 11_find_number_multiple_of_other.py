# Check whether a number is a multiple of another number


try:
    n = int(input("Enter the number here.: "))
    m = int(input("Enter the number here.: "))

    if m == 0:
        print("cannot check multiple of 0")

    elif n%m == 0:
        print(f"{n} is multiple of {m}")

    else:
        print(f"{n} is not multiple of {m}")
except ValueError:
    print("check the number..")
