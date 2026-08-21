# Check whether a number is a prime number

def prime_number():

    try: 
        n = int(input("ENTER THE NUMBER HERE.: "))
        if n <= 1:
            print(f"{n} is not a prime number.")
            
        else:
            for i in range(2,int(n**0.5)+1):
                if n % i == 0 :
                    print(f"{n} is not a prime number.")
                    break
            else:    
                print(f"{n} is  prime number.")        

    except ValueError:
        print("Please enter the valid number here.")


if __name__ == "__main__":
    prime_number()            