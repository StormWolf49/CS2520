#Name: Nikhil Kowdle
#Test 1 - Question 30
#This program contains the task required for this assignment.

#Task 1
#Given a tax table below, write a Python program that asks a user to enter a single person’s taxable income for the year, output the taxable income, tax due, and the after tax income.
#I interpreted the output taxable income to be the same as input taxable income, as that's what I think the question meant.
def price_calculator (preIncome):
    if(0 < preIncome < 9325):
        taxDue = preIncome * 0.1
        postIncome = preIncome - taxDue
    elif(9325 < preIncome < 37950):
        taxDue = 932.50 + ((preIncome - 9325) * 0.15)
        postIncome = preIncome - taxDue
    else:
        taxDue = 5226.25 + ((preIncome - 37950) * 0.25)
        postIncome = preIncome - taxDue
    return preIncome, taxDue, postIncome

'''
Test 1
Taxable Income: 8000, Tax Due: 800.0, After Income Tax: 7200.0

Test 2
Taxable Income: 20050, Tax Due: 2541.25, After Income Tax: 17508.75

Test 3
Taxable Income: 56000, Tax Due: 9738.75, After Income Tax: 46261.25
'''

#Task 2
'''Use a while loop to ask user to repeatedly enter a positive integer n. If a zero or negative number is entered, the while loop terminates.
For each positive number n entered, use a for loop (inside the while loop) to calculate the result = 22 + 32 + ... + n2 + (n+1)2  and display the result.
Test your code once, with the following input numbers: 10, 25, -1.'''
def loop():
    n = int(input("Please enter a positive integer: "))
    while n > 0:        
        result = 0
        for i in range(1, n):
            result += (i + 1) ** 2
        print(result)
        n = int(input("Please enter a positive integer: "))

'''
Test
Please enter a positive integer: 10
385
Please enter a positive integer: 25
5525
Please enter a positive integer: -1
'''

#Task 3
'''Write a function f that takes two parameters x, y with default values for x is 1 and for y is 5, and it returns x2+y3. 
Write a main function that includes the following calls: (1) f()   (2) f(y=1, x=5)   (3) ask a user to enter x, and y and then call f(x,y). 
The main function will print out the return value for each of the function calls respectively. Run the main to execute.'''
def f(x = 1, y = 5):
    return ((x ** 2) + (y ** 3))

'''
Test 1
126

Test 2
26

Test 3
Please enter the x value: 6
Please enter the y value: 9
765
'''

def main():
    preIncome, taxDue, postIncome = price_calculator(8000)
    print(f"Taxable Income: {preIncome}, Tax Due: {taxDue}, After Income Tax: {postIncome}")
    preIncome, taxDue, postIncome = price_calculator(20050)
    print(f"Taxable Income: {preIncome}, Tax Due: {taxDue}, After Income Tax: {postIncome}")
    preIncome, taxDue, postIncome = price_calculator(56000)
    print(f"Taxable Income: {preIncome}, Tax Due: {taxDue}, After Income Tax: {postIncome}")

    loop()

    print(f())
    print(f(y = 1, x=5))
    x = int(input("Please enter the x value: "))
    y = int(input("Please enter the y value: "))
    print(f(x, y))

main()