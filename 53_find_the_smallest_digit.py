# Find the smallest digit in a number

def smallest_digit():
    try:
        num = int(input("Enter the number here.: "))
        n = (str(num))
        smaller = 0
        for i in n:
            if int(i) < smaller:
                smaller = int(i)
                
            
        print("Largest digit:", smaller)

            
    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    smallest_digit()        
