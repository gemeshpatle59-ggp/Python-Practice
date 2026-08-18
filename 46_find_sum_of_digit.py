# Find sum of digits


def len_num():
    try:
        n = int(input("Enter the number here.: "))
        total = 0
        for _ in range(len(str(n))):
            last_digit = n % 10
            total += last_digit
            n = n//10

        print(total)


    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    len_num()        