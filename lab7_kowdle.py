#Name: Nikhil Kowdle
#Lab 7
#This program contains the tasks required for this assignment.

#Task 1
#Allows the logging in and password management of this dictionary based database.
def management():
    usernames = ["Jesse", "Alex", "Ban", "Alice", "Kate", "June", "Nam", "Quan", "Charlie", "Beta"]
    passwords = ["x11yz", "hizzpp", "$$53th", "mddangiagt", "294drdng1", "A@@##3204", "123abc", "gotItRight!!", "marker1324"]
    users = dict(zip(usernames,passwords))
    loop = True
    username = ""
    while loop:
        username = input("Please enter your username: ")
        if username not in users.keys():
            print("Incorrect username, please try again.")
            continue
        for n in range(3):
            password = input("Please enter your password: ")
            if users[username] == password:
                print(f"Login Succesful\nWelcome {username}")
                loop = False
                break
            print(f"Inccorect password, you have {3-(n+1)} tries left")
    else:
        if(input("Would you like to change your password? (Y)es or (N)o\n")) == "Y":
            password = input("Enter new password: ")
            print(f"Old: {list(users.items())}")
            users[username] = password
            print(f"New: {list(users.items())}")

'''
Part 2 Test 1
Please enter your username: Frank 
Incorrect username, please try again.

Part 2 Test 2
lease enter your username: Jesse
Please enter your password: x11yz
Login Succesful
Welcome Jesse

Part 2 Test 3
Please enter your username: Jesse
Please enter your password: 1
Inccorect password, you have 2 tries left
Please enter your password: 2
Inccorect password, you have 1 tries left
Please enter your password: x11yz
Login Succesful
Welcome Jesse

Part 2 Test 4
Please enter your username: Jesse
Please enter your password: 1
Inccorect password, you have 2 tries left
Please enter your password: 2
Inccorect password, you have 1 tries left
Please enter your password: 3
Inccorect password, you have 0 tries left
Please enter your username:

Part 3 Test 1
Please enter your username: Jesse
Please enter your password: x11yz
Login Succesful
Welcome Jesse
Would you like to change your password? (Y)es or (N)o
Y
Enter new password: New
Old: [('Jesse', 'x11yz'), ('Alex', 'hizzpp'), ('Ban', '$$53th'), ('Alice', 'mddangiagt'), ('Kate', '294drdng1'), ('June', 'A@@##3204'), ('Nam', '123abc'), ('Quan', 'gotItRight!!'), ('Charlie', 'marker1324')]
New: [('Jesse', 'New'), ('Alex', 'hizzpp'), ('Ban', '$$53th'), ('Alice', 'mddangiagt'), ('Kate', '294drdng1'), ('June', 'A@@##3204'), ('Nam', '123abc'), ('Quan', 'gotItRight!!'), ('Charlie', 'marker1324')]

Part 3 Test 2
Please enter your username: Alex
Please enter your password: hizzpp
Login Succesful
Welcome Alex
Would you like to change your password? (Y)es or (N)o
Y
Enter new password: Sup
Old: [('Jesse', 'x11yz'), ('Alex', 'hizzpp'), ('Ban', '$$53th'), ('Alice', 'mddangiagt'), ('Kate', '294drdng1'), ('June', 'A@@##3204'), ('Nam', '123abc'), ('Quan', 'gotItRight!!'), ('Charlie', 'marker1324')]
New: [('Jesse', 'x11yz'), ('Alex', 'Sup'), ('Ban', '$$53th'), ('Alice', 'mddangiagt'), ('Kate', '294drdng1'), ('June', 'A@@##3204'), ('Nam', '123abc'), ('Quan', 'gotItRight!!'), ('Charlie', 'marker1324')]
'''

#Task 2
def manip():
    import random
    L1 = [random.randint(1, 100) for _ in range(100)]
    L2 = [x for x in range(1, 100) if ((x % 3 == 0) or (x % 4 == 0))]
    print(f"\nL1: {L1}\n\nL2: {L2}\n")
    S1, S2 = set(L1), set(L2)
    print(f"S1: {S1}\n\nS2: {S2}\n")
    R1 = S1 | S2
    print(f"R1: {len(R1)} elements, {R1}\n")
    R2 = S1 & S2
    print(f"R2: {len(R2)} elements, {R2}\n")
    R3 = S1 - S2
    print(f"R3: {len(R3)} elements, {R3}")

'''
Test
L1: [48, 62, 44, 100, 90, 67, 99, 34, 87, 66, 57, 27, 43, 9, 56, 87, 100, 31, 79, 70, 52, 98, 64, 71, 45, 61, 16, 38, 52, 79, 17, 10, 44, 18, 22, 33, 7, 65, 61, 97, 88, 82, 84, 100, 61, 34, 40, 34, 22, 97, 61, 71, 93, 92, 80, 18, 19, 41, 2, 41, 61, 26, 99, 33, 71, 51, 30, 4, 13, 79, 63, 6, 21, 16, 12, 74, 21, 10, 4, 14, 22, 89, 70, 77, 48, 33, 4, 19, 97, 61, 86, 72, 18, 34, 29, 47, 91, 1, 36, 64]

L2: [3, 4, 6, 8, 9, 12, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 33, 36, 39, 40, 42, 44, 45, 48, 51, 52, 54, 56, 57, 60, 63, 64, 66, 68, 69, 72, 75, 76, 78, 80, 81, 84, 87, 88, 90, 92, 93, 96, 99]

S1: {1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 16, 17, 18, 19, 21, 22, 26, 27, 29, 30, 31, 33, 34, 36, 38, 40, 41, 43, 44, 45, 47, 48, 51, 52, 56, 57, 61, 62, 63, 64, 65, 66, 67, 70, 71, 72, 74, 77, 79, 80, 82, 84, 86, 87, 88, 89, 90, 91, 92, 93, 97, 98, 99, 100}

S2: {3, 4, 6, 8, 9, 12, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 33, 36, 39, 40, 42, 44, 45, 48, 51, 52, 54, 56, 57, 60, 63, 64, 66, 68, 69, 72, 75, 76, 78, 80, 81, 84, 87, 88, 90, 92, 93, 96, 99}

R1: 82 elements, {1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 51, 52, 54, 56, 57, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 86, 87, 88, 89, 90, 91, 92, 93, 96, 97, 98, 99, 100}

R2: 31 elements, {4, 6, 9, 12, 16, 18, 21, 27, 30, 33, 36, 40, 44, 45, 48, 51, 52, 56, 57, 63, 64, 66, 72, 80, 84, 87, 88, 90, 92, 93, 99}

R3: 33 elements, {1, 2, 7, 10, 13, 14, 17, 19, 22, 26, 29, 31, 34, 38, 41, 43, 47, 61, 62, 65, 67, 70, 71, 74, 77, 79, 82, 86, 89, 91, 97, 98, 100}
'''

def main():
    management()
    manip()

main()