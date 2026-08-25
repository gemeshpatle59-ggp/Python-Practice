# Generate Fibonacci series

def fibonacci():
    try:

        n = int(input("Enter the number of terms: "))

        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
    except ValueError:
        print("please enter a valid number")

if __name__ == "__main__":
    fibonacci()