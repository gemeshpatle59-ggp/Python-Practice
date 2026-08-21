# Check whether a number is a perfect number

def perfect_number():

    try:
        n = int(input('Enter the number here.: '))
        sum = 0
        for i in range(1,n):
            if n % i == 0:
                sum += i

        if n == sum:
            print(f"{n} is a perfect number.")   

        else:
            print(f"{n} is not a perfect number.")
    except ValueError:
        print("please enter the valid number in input.")                  

if __name__ == "__main__" :
    perfect_number() 