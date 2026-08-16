# Find the sum of even numbers from 1 to N

def sum_even():

    sum = 0

    try:
        n = int(input("Enter the number here.: "))

        for i in range(0,n+1,2):
            sum += i

        print(f"sum of all even number between 1 to {n} is {sum}")

    except ValueError:
        print("please enter the valid number.")       

if __name__ == "__main__":
    sum_even()         