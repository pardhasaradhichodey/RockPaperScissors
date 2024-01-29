from game.mechanics import get_computer_choice, determine_winner
from game.utils import get_user_choice

def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")
        print(f"{winner}\n")

        if input("Play again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
