# Print multiplication table

def multipliation_table():

    try:
        n = int(input("\nENTER THE NUMBER HERE TO PRINT ITS MULTIPLICATION TABLE.: "))

        print(f"Multiplication table of {n}\n")

        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")

    except ValueError:
        print("please enter the valid number here.")        


if __name__ == "__main__":
    multipliation_table()



