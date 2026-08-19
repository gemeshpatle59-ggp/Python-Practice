# Find the last digit of a number

def len_num():
    try:
        num = int(input("Enter the number here.: "))

        print(f"The last digit of number is {num % 10}")


    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    len_num()        