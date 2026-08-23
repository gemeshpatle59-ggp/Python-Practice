# Count factors of a number

def Factor_num():

    count = 0
    factor = []

    try:
        n = int(input("ENTER A NUMBER HERE.: "))

        for j in range( 1,(n//2)+1):
            if n % j == 0:
                factor.append(j)     
                count += 1
        factor.append(n)
        count += 1
        print(f"The number has {count} factor")   
        print(factor)        


    except ValueError:
        print("Please enter the valid number here.")


if __name__ == "__main__":
    Factor_num()         