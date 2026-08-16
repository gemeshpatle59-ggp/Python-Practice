# Print all even numbers from 1 to N


def even_number(n):
    print("\n====EVEN NUMBERS====")
    for i in range(n+1):
        if i % 2 == 0:
            print(i)

try:
    n = int(input("ENTER THE NUMBER HERE.: "))

except ValueError:
    print("Please enter the valid number.")

even_number(n)
