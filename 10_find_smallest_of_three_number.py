# Find the smallest of three numbers

try:
    n = float(input("Enter the 1st number here.: "))
    m = float(input("Enter the 2st number here.: "))
    o = float(input("Enter the 3st number here.: "))

    if n < m and n < o:
        print(f"{n} is smallest of three numbers.")
      
    elif m < n and m < o :
        print(f"{m} is smallest of three numbers.")
    
    elif m == n and  n == o:
        print(f"{n} {m} {o} all three are same.")
    
    else:
        print(f"{o} is smallest of three numbers.")         

except ValueError:
    print("check the number properly..")    
