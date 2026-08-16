# Print all odd numbers from 1 to N

def odd_number():

    print("=====ODD NUMBERS=====")
    try:
        n = int(input("Enter the numbere here.: "))

        for i in range(1,n+1,2):    
            print(i)

    except ValueError:
        print("please enter proper number.")            

if __name__ == "__main__":
    odd_number()
