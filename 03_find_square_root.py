# WAP to find the square root of any number..

print("\n==================================")
print("-------SQUAREROOT OF NUMBER-------")
print("==================================")


# METHOD 1...

num = float(input("Enter a number here : "))

square = (
    num**(1/2)    
)                     # '**' is use as power of number. ex (n**2) is n power 2

print(f""
      f"\nthe squareroot of no.'{num}' is ==' {square} '=="
      )

# METHOD 2..

import math

num = float(input("Enter a number here : "))

square = (
    math.sqrt(num)
)                            # math.sqrt is to take out squareroot

print(f""
      f"the square root of the no. '{num}' is ==' {square} '=="
      )
