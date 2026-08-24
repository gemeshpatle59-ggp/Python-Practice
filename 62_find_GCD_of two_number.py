# Find GCD of two numbers

def GCD():
    common = 0

    try:
        n = int(input("ENTER A NUMBER HERE.: "))
        m = int(input("ENTER A NUMBER HERE.: "))

        for i in range(1, min(n, m) + 1):
            if n % i == 0 and m % i == 0:
                common = i

    except ValueError:
        print("Please enter the valid number.")     

    print(common)   

if __name__ == "__main__":
    GCD()