# Swap two numbers without a third variable

try:
    n = int(input("Enter the 1st number here.: "))
    m = int(input("Enter the 2nd number here.: "))

    n , m = m ,n

    print(f"1st_n0. = {n}\n2nd_no. = {m}")

except ValueError:
    print("Please enter the vaild number in input.")    