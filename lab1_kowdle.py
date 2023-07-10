#Name: Nikhil Kowdle
#Lab 1
#This program will display my dream job goal settings

#Stores the user input of their name in the name variable.
name = input("Please enter your name: ")
#Stores the user input of their age in the age variable after converting it into an integer.
age = int(input("Please enter your age: "))
#Stores the user input of their company in the company variable.
company = input("Enter the company you wish to work: ")
#Stores the user input of their salary in the salary variable after converting it into an float.
salary = float(input("Enter the annual salary you wish to earn in dollars: "))

#Prints out the stored data in a set of formatted print statements, including dividing the annual 
#salary by 12 to get the monthly salary and then rounding it to 2 decimal points.
print("Hello!")
print(f"My name is {name}, my age is {age}")
print(f"I hope to work for {company} and earn ${round(salary / 12, 2)} a month.")

'''
Test #1
Please enter your name: Alice Wonderland
Please enter your age: 20
Enter the company you wish to work: Google
Enter the annual salary you wish to earn in dollars: 98576
Hello!
My name is Alice Wonderland, my age is 20
I hope to work at Google and earn $8214.67

Test #2
Please enter your name: Nikhil
Please enter your age: 22
Enter the company you wish to work: Boston Dynamics
Enter the annual salary you wish to earn in dollars: 100000
Hello!
My name is Nikhil, my age is 22
I hope to work for Boston Dynamics and earn $8333.33 a month.
'''
