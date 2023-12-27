"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
"""

"""
Extras:

1. If the number is a multiple of 4, print out a different message.

2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


#Solution
import numbers

num = int(input("Give me a number: "))

if num%2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#Or 

if (num/2).is_integer() is True:
    print("This is an even number")
else:
    print("This is an odd number.")



#Solution with extra 1
if num%2 == 0:
    if (num/4).is_integer() is True:
        print("\nThis is an even number. It is also a multiple of 4.")
    else:
        print("\nThis is an even number. It is not a multiple of 4.")
else:
    if (num/4).is_integer() is True:
        print("\nThis is an odd number. It is also a multiple of 4.")
    else:
        print("\nThis is an odd number. It is not a multiple of 4.")


#Solution with extra 2
num_2 = int(input("\nGive me a number (X): "))
check = int(input("Give me a number to divide by: "))


if (num_2/check).is_integer() is True:
    print(f'\nThe number {num_2} is a multiple of {check}.')
else:
    print(f'\nThe number {num_2} is not a multiple of {check}.')
