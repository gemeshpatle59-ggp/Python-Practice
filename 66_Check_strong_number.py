# Check whether a number is a strong number

def Strong_number():
    try:
        num = int(input("Enter the number here.: "))

        if num < 0:
            print("strong number cannot be nagative. ")
            return
        
        n = len(str(num))
        m = str(num)
        Total = 0
        for j in range(n):
            fact = 1
            for i in range(1,(int(m[j])+1)):
                fact *= i
            Total += fact    
        if num == Total:
            print(f"{num} is a Strong number..")
        else:
            print(f"{num} is not a strong number..")    

        
    except ValueError:
        print("Plaese enter the valid number.")

if __name__ == "__main__":
    Strong_number()        