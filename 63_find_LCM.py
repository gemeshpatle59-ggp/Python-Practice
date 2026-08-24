# Find LCM of two numbers

def LCM():
    common = 0

    try:
        n = int(input("ENTER A NUMBER HERE.: "))
        m = int(input("ENTER A NUMBER HERE.: "))
        i = 1
        while True:
            if n * i % m == 0:
                common = n*i
                break
            i += 1
            
    

    except ValueError:
        print("Please enter the valid number.")     

    print(common)   

if __name__ == "__main__":
    LCM()