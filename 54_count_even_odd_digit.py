# Count even and odd digits

def even_odd():
    try:
        num = int(input("Enter the number here.: "))
        n = (str(num))
        even = 0
        odd = 0
        for i in n:
            if int(i) % 2 == 0:
                even += 1
            if int(i) % 2 != 0:
                odd += 1    
                
            
        print("Even digit :", even)
        print("Odd digit :", odd)
            
    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    even_odd()   