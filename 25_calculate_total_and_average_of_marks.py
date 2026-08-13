# Calculate total and average of marks

try:
    n = list(map(int,input("Enter all obtain marks here.: ").split()))
    m = int(input("Enter the marks obtained in all subjects to calculate the average marks here.: "))

    total = 0

    for i in range(len(n)):
        total += n[i]

    average = total/len(n)

    print(f"The total mark is {total} and the average of marks all subject is {average}")

except ValueError:
    print("Enter the number correctly")
    
