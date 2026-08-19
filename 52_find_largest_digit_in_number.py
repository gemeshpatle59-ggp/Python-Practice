# Find the largest digit in a number

def larger_digit():
    try:
        num = int(input("Enter the number here.: "))
        n = (str(num))
        larger = 0
        for i in n:
            if int(i) > larger:
                larger = int(i)
                
            
        print("Largest digit:", larger)

            
    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    larger_digit()        
