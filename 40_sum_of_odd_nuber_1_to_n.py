# Find the sum of odd numbers from 1 to N

def sum_odd():

    sum = 0

    try:
        n = int(input("Enter the number here.: "))

        for i in range(1,n+1,2):
            sum += i

        print(f"sum of all odd number between 1 to {n} is {sum}")

    except ValueError:
        print("please enter the valid number.")       

if __name__ == "__main__":
    sum_odd()         