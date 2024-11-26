"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

import math,os

l1 = float(input("Enter first length: "))
l2 = float(input("Enter second length: "))
q1 = False

while q1 == False:   
    if q1 == False:
        ishyp = input("Is one of the lengths the hypotenuse of a right triangle? ")
        if "yes" in ishyp:
            ishyp = True
            q1 = True
        elif "no" in ishyp:
            ishyp = False
            q1 = True
        else:
            os.system('cls')
            print("Answer using yes or no")

if ishyp:
    if l1 > l2:
        hyp = l1
        length = l2
    else:
        hyp = l2
        length = l1
    l3 = math.sqrt(math.pow(hyp, 2) - math.pow(length, 2))
elif ishyp == False:
    l3 = math.sqrt(math.pow(l1, 2) + math.pow(l2, 2))
round(l3, 1)
print(f'The missing length is {l3}.')
exit()

#done