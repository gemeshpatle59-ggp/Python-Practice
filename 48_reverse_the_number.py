# Reverse a number

def len_num():
    try:
        n = int(input("Enter the number here.: "))
        reverse = 0
        for _ in range(len(str(n))):
            last_digit = n % 10
            reverse = (reverse * 10) + last_digit
            n = n//10

        print(reverse)


    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    len_num()        