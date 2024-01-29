def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Choose rock, paper, or scissors: ").lower()
    return choice
