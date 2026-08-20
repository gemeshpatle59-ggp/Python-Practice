# Check whether a number is an Armstrong number

def len_num():
    try:
        num = int(input("Enter the number here.: "))
        n = num
        sum_square = 0
        for _ in range(len(str(n))):
            last_digit = n % 10
            sum_square += last_digit**(len(str(num)))
            n = n//10

        if sum_square == num:
            print(f"The number is Armstrong")
        else:
            print("The number is not Armstrong")    


    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    len_num()        