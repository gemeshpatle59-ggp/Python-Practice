# Calculate percentage

try:
    n = int(input("Enter the Total number here.: "))    
    m = int(input("Enter the obtain number here.: "))
    
    percentage = m/n*100


    print(f"The percentage is {percentage:.2f}")

except ValueError:
    print("Enter the correct value")



    