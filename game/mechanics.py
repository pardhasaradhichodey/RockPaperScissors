import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if ((user_choice == "rock" and computer_choice == "scissors") or 
        (user_choice == "scissors" and computer_choice == "paper") or 
        (user_choice == "paper" and computer_choice == "rock")):
        return "You win!"

    return "Computer wins!"
