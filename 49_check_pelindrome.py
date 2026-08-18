# Check whether a number is a palindrome

def len_num():
    try:
        num = int(input("Enter the number here.: "))
        n = num
        reverse = 0
        for _ in range(len(str(n))):
            last_digit = n % 10
            reverse = (reverse * 10) + last_digit
            n = n//10

        if reverse == num:
            print(f"The number is pelindrome")
        else:
            print("The number is not pelindrome")    


    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    len_num()        