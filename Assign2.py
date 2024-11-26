"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

import math

l1 = float(input("Enter first length: "))
l2 = float(input("Enter second length: "))
q1 = False


try:
    ishyp = input("Is one of the lengths the hypotenuse of a right triangle? ")
    if "yes" in ishyp:
        ishyp = True
        q1 = True
    elif "no" in ishyp:
        ishyp = False
        q1 = True
except:
    