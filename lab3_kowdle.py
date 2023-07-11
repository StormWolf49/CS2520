#Name: Nikhil Kowdle
#Lab 3
#This program contains the 4 tasks required for this assignment.

#Task 1
#While loop that runs forever unless the player specifically replies to break the loop.
while True :
    #Starts the game and asks the player for their choice.
    print("welcome to the rock, paper, scissors game.")
    plyChoice = input("Please select type your choice between 'Rock', 'Paper', or 'Scissors': ")
    #Imports the random function and setups up the computer's randomized choice.
    import random
    cmpChoice = random.choice(['Rock', 'Paper', 'Scissors'])

    #Tells the player if they won, tied, or lost according to the computer and their choice.
    print(f"Player: {plyChoice} vs Computer: {cmpChoice}")
    if (plyChoice == 'Rock' and cmpChoice == 'Scissors') or (plyChoice == 'Paper' and cmpChoice == 'Rock') or (plyChoice == 'Scissors' and cmpChoice == 'Paper') :
        print("You win!")
    elif plyChoice == cmpChoice :
        print("It's a tie!")
    else :
        print("You lose.")

    #Asks the player if they want to play again and breaks the loop if they don't.
    more = input("Do you want to play again?(Yes or No) ")
    if more == 'No' :
        break

'''
Test
welcome to the rock, paper, scissors game.
Please select type your choice between 'Rock', 'Paper', or 'Scissors': Rock
Player: Rock vs Computer: Scissors    
You win!
Do you want to play again?(Yes or No) Yes
welcome to the rock, paper, scissors game.
Please select type your choice between 'Rock', 'Paper', or 'Scissors': Rock
Player: Rock vs Computer: Paper       
You lose.
Do you want to play again?(Yes or No) Yes
welcome to the rock, paper, scissors game.
Please select type your choice between 'Rock', 'Paper', or 'Scissors': Rock
Player: Rock vs Computer: Paper
You lose.
Do you want to play again?(Yes or No) Yes
welcome to the rock, paper, scissors game.
Please select type your choice between 'Rock', 'Paper', or 'Scissors': Rock
Player: Rock vs Computer: Rock
It's a tie!
Do you want to play again?(Yes or No) Yes
welcome to the rock, paper, scissors game.
Please select type your choice between 'Rock', 'Paper', or 'Scissors': Rock
Player: Rock vs Computer: Scissors
You win!
Do you want to play again?(Yes or No) No
'''

#Task 2
#Takes the user input of the count and total, and either prints 0 as the average if the count is 0, or divides the total by the count.
count = int(input("Please enter the number of items purchased "))
total = float(input("Please enter the total cost "))
print("Average =", 0 if count == 0 else total/count ) #place a conditional expression inside

'''
Test 1
Please enter the number of items purchased 13
Please enter the total cost 35.2
Average = 2.707692307692308

Test 2
Please enter the number of items purchased 0
Please enter the total cost 5
Average = 0

Test 3
Please enter the number of items purchased 7
Please enter the total cost 49
Average = 7.0
'''

#Task 3
#Prints all the odd numbers from 1 to 50
for j in range(1, 50, 2) :
    print(j, end=' ')

'''
Test
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49
'''

#Task 4
#Imports the random function and randomly picks the letter searched for from string with all 26 letters.
import random
letters = "abcdefghijklmnopqrstuvwxyz"
seed = random.choice(letters)
#Asks the user for the sentence that will be searched for the seed letter chosen previously.
sentence = input("Please provide the sentence to search: ")
#Loops through the sentence looking for the letter.
for e in range(0, len(sentence)) :
    #At the first instance of the letter found, break the loop and print out the letter saying it was found and the sentence.
    if sentence[e] == seed :
        print(f"Letter {seed} found in {sentence}")
        break
#Print out the letter saying it was not found and the sentence.
else :
    print(f"Letter {seed} not found in {sentence}")

'''
Test 1
Please provide the sentence to search: poggers
Letter r found in poggers

Test2
Please provide the sentence to search: poggers
Letter y not found in poggers
'''