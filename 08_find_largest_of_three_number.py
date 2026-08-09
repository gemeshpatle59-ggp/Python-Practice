# Find the largest of three numbers
try:
    n = float(input("Enter the 1st number here.: "))
    m = float(input("Enter the 2st number here.: "))
    o = float(input("Enter the 3st number here.: "))

    if n > m and n > o:
        print(f"{n} is largest of all three numbers.")

    elif m > n and m > o:
        print(f"{m} is largest of all three numbers.")

    elif m == n and m == o:
        print(f"{n} {m} {o} all three are equal")

    else:
        print(f"{o} is largest of all three number.")            

except ValueError:
    print("check the number poperly")
