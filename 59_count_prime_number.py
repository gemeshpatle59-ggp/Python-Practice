# Count prime numbers from 1 to N

def prime_number():

    count = 0

    try:
        n = int(input("ENTER A NUMBER HERE.: "))

        for j in range( 1,n+1):
            for i in range(2,j):
                if j % i == 0:
                    break
            else:
                if j>1:
                    count += 1

        print(f"There are {count} prime number betn 1 To {n}")            


    except ValueError:
        print("Please enter the valid number here.")


if __name__ == "__main__":
    prime_number()         