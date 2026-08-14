# Calculate salary after deduction 
try:
    n = int(input('Enter the salary amount here.: '))
    m = int(input('Enter the PF deduction percentage  here.: '))
    o = int(input("Enter the tax deducation percentage here .: "))
    p = int(input("Enter the other deducation amount here .: "))

    pf_deducation = n *(m/100)
    tac_deducation = n * (o/100)

    total_deducation = pf_deducation + tac_deducation + p

    net_salary = n - total_deducation

    print(f"The net salary is {net_salary:.2f}")

except ValueError:
    print("please enter the vaild number in input..")    