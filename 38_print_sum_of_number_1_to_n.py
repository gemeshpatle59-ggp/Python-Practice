# Find the sum of numbers from 1 to N

def sum_numbers():

    sum = 0

    try:
        n = int(input("ENTER THE NUMBER HERE.: "))

        for i in range(n+1):
            sum += i

        print(f"sum of all number between 1 and {n} is {sum}")

    except ValueError:
        print("please enter the valid number..")    

if __name__ == "__main__":
    sum_numbers()
