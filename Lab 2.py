#Name: Nikhil Kowdle
#Lab 2
#This program contains the 3 tasks required for this assignment.

#Task 1
#Stores the user input of how many apples in the apples variable after converting it into an integer.
apples = int(input("How many apples you have bought? "))
#Stores the user input of the total cost for the apples in the total variable after converting it into float.
total = float(input(f"How much you've paid for the {apples} apples: $"))
#Prints out the averae price of the apples after calculating it and rounding to 2 decimal points.
print(f"In average, each apple costs ${round(total / apples, 2)}")
"Prints out how many apples each child gets by dividing the number of apples by 3, and a modulo calculation to figure out how many apples would be leftover."
print(f"We have 3 children here, so each get {apples // 3} apples with {apples % 3} leftover.")
print("Thank you for shopping!")

'''
Test 1
How many apples you have bought? 13
How much you've paid for the 13 apples: $5.27
In average, each apple costs $0.41
We have 3 children here, so each get 4 with 1 leftover.
Thank you for shopping!

Test 2
How many apples you have bought? 84
How much you've paid for the 84 apples: $23.6
In average, each apple costs $0.28
We have 3 children here, so each get 28 apples with 0 leftover.
Thank you for shopping!

Test 3
How many apples you have bought? 8
How much you've paid for the 8 apples: $6.94
In average, each apple costs $0.87
We have 3 children here, so each get 2 apples with 2 leftover.
Thank you for shopping!
'''

#Task 2
#Stores the user input of the present value as a float.
PV = float(input("What's the present value? "))
#Stores the user input of the intrest rate as a float.
INT = float(input("What's the interest rate (percentage)? "))
#Stores the user input of the number of years as a float.
YRS = float(input("How many years? "))
#Caluclates and prints the future value.
print(f"${round(PV * ((1 + (INT / 100)) ** YRS), 2)}")

'''
Test 1
What's the present value? 1000
What's the interest rate (percentage)? 5
How many years? 10
$1628.89

Test 2
What's the present value? 2500
What's the interest rate (percentage)? 3
How many years? 30
$6068.16

Test 3
What's the present value? 420
What's the interest rate (percentage)? 6.9
How many years? 7
$670.03
'''

#Task 3
#Swaps the user input values of x and y with each other.
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
print("Before swapping: ", x, y)
x, y = y, x
print ("After swapping: ", x, y)

'''
Test 1
Enter the first number: 8
Enter the second number: 5
Before swapping:  8.0 5.0
After swapping:  5.0 8.0

Test 2
Enter the first number: 7
Enter the second number: 3
Before swapping:  7.0 3.0
After swapping:  3.0 7.0
'''

#Task 4
#Accepts and stores two strings and concatenates them together and concatenates the first string together 3 times.
first = input("Enter the first string: ")
second = input("Enter the second string: ")
print(first + second)
print (first * 3)

'''
Test 1
Enter the first string: good
Enter the second string: morning
goodmorning
goodgoodgood

Test 2
Enter the first string: second
Enter the second string: test
secondtest
secondsecondsecond
'''