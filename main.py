from game.mechanics import get_computer_choice, determine_winner
from game.utils import get_user_choice

def main():
    rounds = int(input("How many rounds would you like to play? "))
    user_wins = 0
    computer_wins = 0

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")
        print(f"{winner}\n")

        if winner == "You win!":
            user_wins += 1
        elif winner == "Computer wins!":
            computer_wins += 1

    if user_wins > computer_wins:
        print(f"You won the game {user_wins} to {computer_wins}!")
    elif computer_wins > user_wins:
        print(f"Computer won the game {computer_wins} to {user_wins}!")
    else:
        print(f"The game is a tie {user_wins} to {computer_wins}.")

if __name__ == "__main__":
    main()
