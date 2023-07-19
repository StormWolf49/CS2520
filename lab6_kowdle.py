#Name: Nikhil Kowdle
#Lab 6
#This program contains the task required for this assignment.

#Task 1
def L1():
    list = []
    n = float(input("Please enter a positive number: "))
    while n >= 0:        
        list.append(n)
        n = float(input("Please enter a positive number: "))
    print(list)

import random
def L2():
    n = int(input("Please enter a positive integer: "))
    list = [round(random.uniform(1, 10), 2) for _ in range(n)]
    print(list)

'''

'''

#Task 2


'''

'''

#Task 3

'''

'''

def main():
    L1()
    L2()

main()