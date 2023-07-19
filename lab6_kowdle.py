#Name: Nikhil Kowdle
#Lab 6
#This program contains the task required for this assignment.

#Task 1
#Creates List 1 which takes positive numbers and keeps adding them to the list until it gets a negative number.
def L1():
    list = []
    n = float(input("Please enter a positive number: "))
    while n >= 0:        
        list.append(n)
        n = float(input("Please enter a positive number: "))
    print(list)

#Creates List 2 by taking an integer and creating a list of that length filled with random floats from the 1 to 10 range.
def L2():
    import random
    n = int(input("Please enter a positive integer: "))
    list = [round(random.uniform(1, 10), 2) for _ in range(n)]
    print(list)

'''
L1 Test 1
Please enter a positive number: 10.2
Please enter a positive number: 20.1
Please enter a positive number: 15.2
Please enter a positive number: -2.5
[10.2, 20.1, 15.2]

L1 Test 2
Please enter a positive number: -4
[]

L1 Test 3
Please enter a positive number: 4
Please enter a positive number: 8
Please enter a positive number: 2.3
Please enter a positive number: 6.4
Please enter a positive number: 93.2
Please enter a positive number: 0
Please enter a positive number: 2.3
Please enter a positive number: 5.1
Please enter a positive number: 45.7
Please enter a positive number: -1
[4.0, 8.0, 2.3, 6.4, 93.2, 0.0, 2.3, 5.1, 45.7]

L2 Test 1
Please enter a positive integer: 5
[5.38, 9.06, 9.52, 1.9, 6.41]

L2 Test 2
Please enter a positive integer: 0
[]

L2 Test 3
Please enter a positive integer: 7
[1.61, 7.44, 5.32, 2.66, 2.7, 7.98, 1.51]
'''

#Task 2
#Takes a string and converts into a tuple then counts the number of vowels and prints it.
def vowels():
    word = input("Please enter the desired string: ")
    search = tuple(word)
    vowels = 0
    for w in search:
        if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
            vowels += 1
    print(f'{word} has {vowels} vowels')

'''
Test 1
Please enter the desired string: hello
hello has 2 vowels

Test 2
Please enter the desired string: humongous
humongous has 4 vowels

Test 3
Please enter the desired string: gigantic
gigantic has 3 vowels
'''

#Task 3
#Creates two different lists, the first being a list of tuples pairing the semesters and enrollments list. 
#The second list is a list of tuples that includes the indexes starting from 1 and the semesters list.
def sequence():
    semesters = ['Fall', 'Winter', 'Spring', 'Summer']
    enrollments = [215, 21, 187, 58]
    print(list(zip(semesters, enrollments)))
    print(list(enumerate(semesters, start=1)))

'''
Test
[('Fall', 215), ('Winter', 21), ('Spring', 187), ('Summer', 58)]
[(1, 'Fall'), (2, 'Winter'), (3, 'Spring'), (4, 'Summer')]
'''

def main():
    #Task 1 Main
    L1()
    L1()
    L1()
    L2()
    L2()
    L2()

    #Task 2 Main
    vowels()
    vowels()
    vowels()

    #Task 3 Main
    sequence()

main()