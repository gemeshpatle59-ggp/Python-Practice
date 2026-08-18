# Find product of digits

def len_num():
    try:
        n = int(input("Enter the number here.: "))
        product = 1
        for _ in range(len(str(n))):
            last_digit = n % 10
            product *= last_digit
            n = n//10

        print(product)


    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    len_num()        