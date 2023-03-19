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
    user_input = input(f"Please choose one of the following options: {ROCK}, {SCISSORS}, {PAPER}\n").lower()
    return user_input

def find_game_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print_winner_message('No winner this time, sorry!!!')
    elif user_choice == ROCK and computer_choice == SCISSORS:
        print_winner_message(user_name)
    elif user_choice == PAPER and computer_choice == ROCK:
        print_winner_message(user_name)
    elif user_choice == SCISSORS and computer_choice == PAPER:
        print_winner_message(user_name)
    else:
        print_winner_message('Computer')

# Possible computer choices
options = [ROCK, PAPER, SCISSORS]

# Ask the player to write player's name
user_name = input("Please enter players name:\n")

# Ask the player to choose rock, paper, or scissors
user_choice = get_user_input()

# Check if the player's choice is valid
while user_choice not in options:
    print(f"Don't cheat, {user_name}. Enter valid option.")
    # Ask the player to choose rock, paper, or scissors
    user_choice = get_user_input()

# The computer chooses a random option
computer_choice = random.choice(options)

# Start game output
print_star(30)

# Print out the computer's choice
print(f"\nThe computer's choice: {computer_choice.capitalize()}")

#Print out the user's choice
print(f"{user_name}'s choice: {user_choice.capitalize()}")

# Determine the winner of the game
find_game_winner(user_choice, computer_choice)

#Close game output
print_star(30)

