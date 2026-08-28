# Check whether a number is a neon number

num = -9

def neon_number(num):
    if num < 0:
        print(f"{num} is not a neon number..")
        return
    n = num ** 2
    total = 0
    while n > 0:
        last_digit = n % 10
        total += last_digit
        n = n // 10

    if num ==  total:
        print(f"{num} is a neon number..") 

    else:
        print(f"{num} is not a neon number..")

neon_number(num)           