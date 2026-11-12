def calulator(a , b):

    print("'+' for addition")
    print("'-' for subtraction")
    print("'*' for multiplication")
    print("'/' for division")

    sign = input("Enter the sign here.: ")

    while True:
        if sign == "+":
            return(a + b)

        elif sign == "-":
            return(a - b)

        elif sign == "*":
            return(a * b)

        elif sign == "/":
            return(a / b)

        else:
            print("please choose correct sign ('-','+','*','/')")

a = int(input("Enetr a number.: "))
b = int(input("Enter a second number here.: "))
print(calulator(a,b))
