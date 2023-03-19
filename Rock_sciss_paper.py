import random

ROCK = 'rock'
SCISSORS = 'scissors'
PAPER = 'paper'

def print_star(times):
    for i in range(times):
        print("*", end="")

def print_winner_message(name: str):
    print(f"\nAND THE WINNER IS: {name}")

def get_user_input():
    user_input = input(f"\nPlease choose one of the following options: {ROCK}, {SCISSORS}, {PAPER} \n").lower()
    return user_input

def verify_user_option(user_choice, user_name, options):
    while user_choice not in options:
        print(f"Don't cheat, {user_name}. Enter valid option.")

        #Ask user to choose rock, scissors or paper
        user_choice = get_user_input()
    return user_choice


def find_game_winner(user_choice, computer_choice, user_name):
    if user_choice == ROCK and computer_choice == SCISSORS:
        print_winner_message(user_name)
        return user_name
    elif user_choice == PAPER and computer_choice == ROCK:
        print_winner_message(user_name)
        return user_name
    elif user_choice == SCISSORS and computer_choice == PAPER:
        print_winner_message(user_name)
        return user_name
    elif user_choice == computer_choice:
        print_winner_message('No one wins! It is tie! Playing again...')
        return 'tie'
    else:
        print_winner_message('Computer')
        return 'Computer'

# Possible computer choices
options = [ROCK, SCISSORS, PAPER]

# Ask the player to write player's name
user_name = input("Please enter players name:\n")

while True: 
    # Ask the player to choose rock, scissors or paper
    user_choice = get_user_input()

    # Check if the player's choice is valid
    user_choice = verify_user_option(user_choice, user_name, options)

    # The computer chooses a random option
    #computer_choice = random.choice(options)
    computer_choice = 'scissors'

    print_star(30)

    # Print out the computer's choice
    print(f"\nThe computer's choice: {computer_choice.capitalize()}")

    #Print out the user's choice
    print(f"{user_name}'s choice: {user_choice.capitalize()}")

    winner = find_game_winner(user_choice, computer_choice, user_name)

    if winner != 'tie':
        print_star(30)
        print(f"\n{winner} wins! Congratulations!")
        break

#Close game output
print_star(30)

