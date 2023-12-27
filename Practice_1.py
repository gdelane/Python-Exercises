"""Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
If you want to do this in a generic way, see exercise 39."""

"""Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)

2. Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)"""


#Solution
import numbers

name = input("Hello. What is your name? ")
age = int(input("How old are you? "))
current_year = int(2023)
birth_year = int(current_year-age)
year_100 = int(birth_year + 100)

print(f'Hello {name}. You will be 100 years old in the year {year_100}.')




#Solution with extra 1

name = input("Hello. What is your name? ")
age = int(input("How old are you? "))
num = input("Give me a number: ")
current_year = int(2023)
birth_year = int(current_year-age)
year_100 = int(birth_year + 100)

x = 0

while x < int(num):
    print(f'Hello {name}. You will be 100 years old in the year {year_100}.')
    x += 1


#Solution with extra 2

name = input("Hello. What is your name? ")
age = int(input("How old are you? "))
num = input("Give me a number: ")
current_year = int(2023)
birth_year = int(current_year-age)
year_100 = int(birth_year + 100)

x = 0

while x < int(num):
    print(f'\nHello {name}. You will be 100 years old in the year {year_100}.')
    x += 1
