# Print prime numbers from 1 to N

def prime_number():
    try:
        n = int(input("ENTER A NUMBER HERE.: "))

        for j in range( 1,n+1):
            for i in range(2,j):
                if j % i == 0:
                    break
            else:
                if j>1:
                    print(f"{j}")


    except ValueError:
        print("Please enter the valid number here.")


if __name__ == "__main__":
    prime_number()        