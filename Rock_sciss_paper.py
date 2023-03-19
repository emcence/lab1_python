import random

def print_message(name:str):
        print("****AND THE WINNER IS*******")
        print(f'*******{name} ********')
        print("*************************")  

# Possible computer choices
options = ['rock', 'paper', 'scissors']

# Ask the player to choose rock, paper, or scissors
user_choice = input("Please choose one of the following options: rock, scissors, paper\n").lower()

# Check if the player's choice is valid
if user_choice not in options:
    print("Invalid choice!")
else:
    # The computer chooses a random option
    computer_choice = random.choice(options)
    
    # Print out the computer's choice
    print("The computer chose: ", computer_choice)
    
    #Print out the user's choice
    print("User chose:", user_choice)

    # Determine the winner of the game
    if user_choice == computer_choice:
        print_message('No winner this time, sorry')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print_message('Emi')
    elif user_choice == 'paper' and computer_choice == 'rock':

        print_message('Emi')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print_message('Emi')
    else:
        print_message('Computer')