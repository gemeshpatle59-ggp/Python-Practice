# Find power of a number using a loop

def power():

    try:
        n = int(input("\nENTER THE NUMBER HERE.: "))
        m = int(input("ENTER THE POWER HERE.: "))

        power = 1

        for _ in range(1,m+1):
            power *= n

        print(power)

    except ValueError:
        print("please enter the valid number here.")        


if __name__ == "__main__":
    power()

