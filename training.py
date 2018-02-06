"""
For this problem you are going to make a program that simulates the output of a vending machine that only takes in
coins of American currency.
1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
 for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
 Use your knowledge of if, elif, and else statements to complete this part of the problem. Your code should
 have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
 input number.
 Vending Machine:
 1.water = $1.00
 2.cola = $1.50
 3.gatorade = $2.00
2.After placing an order, the user should be prompted to enter inputs 4 times:
 1.The first time, the user should be prompted to enter the number of quarters they put in the machine. Assign this
 number to a variable as an integer.
 2.The second time, the user should be prompted to enter the number of dimes they put in the machine. Assign this
 number to a variable as an integer.
 3.The third time, the user should be prompted to enter the number of nickles they put in the machine. Assign this
 number to a variable as an integer.
 4.The fourth time, the user should be prompted to enter the number of pennies they put in the machine. Assign this
 number to a variable as an integer.
3.Create a variable to hold the total value of all the coins the user has put into the machine.
4.Use flow control statements to print the user's change or output a message asking the user to try again depending
 on whether the total value of the coins the user has put into the machine is enough to pay for the item they ordered.
New knowledge for this problem:
1.%f specifier works like the %s specifier except that %f is used whenever you want to replace a placeholder with a
 float instead of a string.
2.import sys and sys.exit(). import sys should be typed at the top of your program since you must have the code
import
 sys in your program to use sys.exit(). sys.exit() ends a program and outputs whatever message is within its
 parentheses.
3.int() works similarly to str() except that int() turns whatever is in its parenthesis to an integer instead of a
 string
"""

# 1.

# must have import sys in program to use sys.exit()

import sys

# asks the user to enter their input as an integer with 1 corresponding to water, 2 corresponding to cola, and 3
# corresponding to gatorade.  Note that int() is used to change the user's input (shich is a string) to an integer.
order = int(input("Enter your order number as an integer.(1,2,or3)"))

if order == 1:
    #water is $1.00, thus a varible, thisPrice is created and assigned 1.00 if the user enters 1 for water
    thisPrice = 1.00
elif order == 2:
    # cola is $1.50
    thisPrice = 1.50
elif order == 3:
    # gatorade is $2.00
    thisPrice = 2.00
else:
    #ends the program and prints the message "Please try again." if order does not equal 1, 2, or 3
sys.exit("Please try again")