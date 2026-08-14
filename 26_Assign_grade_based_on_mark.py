# Assign grade based on marks

try:

    n  = int(input("Enter your marks here.: "))

    if n >= 90:
        print(f"Your marks are '{n}' and your grade is 'A+'")
    elif n >= 80:
        print(f"Your marks are '{n}' and your grade is 'A'")        
    elif n >= 70:
        print(f"Your marks are '{n}' and your grade is 'B+'")
    elif n >= 60:
        print(f"Your marks are '{n}' and your grade is 'B'")
    elif n >= 50:
        print(f"Your marks are '{n}' and your grade is 'C+'")
    elif n >= 40:
        print(f"Your marks are '{n}' and your grade is 'C'")
    elif n >= 30:
        print(f"Your marks are '{n}' and your grade is 'D+'")
    elif n >= 20:       
        print(f"Your marks are '{n}' and your grade is 'D'")    
    else:
        print(f"Your marks are '{n}' and your grade is 'F'")        

except ValueError:
    print("Please enter a valid number for marks.")        