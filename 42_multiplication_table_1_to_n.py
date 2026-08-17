# Print multiplication tables from 1 to n 

def multipliation_table():

    try:
        n = int(input("\nENTER THE NUMBER HERE TILL YOU WANT TO PRINT  MULTIPLICATION TABLE.: "))


        for i in range(1,n+1):
            print(f"\nMultiplication table of {i}\n")

            for j in range(1,10):
                print(f"{n} x {j} = {n*j}")
            

    except ValueError:
        print("please enter the valid number here.")        


if __name__ == "__main__":
    multipliation_table()
