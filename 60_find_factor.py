# Find factors of a number

def Factor_num():

    factor = []

    try:
        n = int(input("ENTER A NUMBER HERE.: "))

        for j in range( 1,(n//2)+1):
            if n % j == 0:
                factor.append(j)  

        factor.append(n)        
        print(f"\nFactor of {n} are...")
        print(factor)

    except ValueError:
        print("Please enter the valid number here.")


if __name__ == "__main__":
    Factor_num()         
