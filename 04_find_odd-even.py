# Check whether a number is even or odd

try:
    n = int(
        input
            ("Enter the number here.: ")
        )

    if n%2 == 0:
        print(f""
              f"{n} is a even number"
              )

    else:
        print(f""
              f"{n} is a odd number"
              )    

except ValueError:
    print(""
    "Enter integer number.."
    )    
