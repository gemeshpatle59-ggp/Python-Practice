# Count digits in a number


def len_num():
    try:
        n = int(input("Enter the number here.: "))

        def len_nu(n):
            if n == 0:
                return 0 
        
            return 1 + len_nu(n//10)
            
        print(f"the digit in number is {len_nu(n)}")

    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    len_num()        