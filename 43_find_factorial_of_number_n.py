# Find factorial of a number


def factorial():

    try:
        n = int(input("\nENTER THE NUMBER HERE TO FIND ITS FACTORIAL.: "))


        def fact(n):
            if n == 1:
                return  1
            
            return n * fact(n-1)


        print(fact(n))

    except ValueError:
        print("please enter the valid number here.")        


if __name__ == "__main__":
    factorial()


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))