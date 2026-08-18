# Find the first digit of a number

def len_num():
    try:
        num = int(input("Enter the number here.: "))
        n = len(str(num))
        last_digit = n - 1
        print(f"The first digit of number is {num // 10**last_digit}")


    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    len_num()        