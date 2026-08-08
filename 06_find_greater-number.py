# Find the largest of two number...


try:

    n = float(
        input(
            "Enter the 1st number here..: "
        )
            )
    m = float(
        input(
            "Enter the 2nd number here..: "
        )
            )
    if n > m:
        print(f""
              f"{n} is greater than {m}"
              )

    elif n < m:
        print(f""
              f"{m} is greater than {n}"
              ) 
    else:
        print(f"{n} and {m} both are equal")       

except ValueError:
    print("enter nuber properly..")
