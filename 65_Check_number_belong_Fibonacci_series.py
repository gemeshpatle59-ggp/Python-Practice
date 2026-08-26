# Check whether a number belongs to Fibonacci series

def fibonacci():
    try:

        n = int(input("Enter the number here: "))

        if n < 0:
            print(f"{n} does not belong to Fibonacci series.")
            return
            

        a = 0
        b = 1

        while a<=n:
            if n == a:
                print(f"{n} belong to fibnoacci number.. ")
                break
            a,b = b,a+b
        else:
            print(f"{n} do not belong to fibnoacci number .")
    

    except ValueError:
        print("please enter a valid number")

if __name__ == "__main__":
    fibonacci()