import random
def get_user_choice():
    print("Choose rock, paper, or scissors:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = input("Enter your choice (1/2/3): ")
    if user_choice == "1":
        return "rock"
    elif user_choice == "2":
        return "paper"
    elif user_choice == "3":
        return "scissors"
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? \n enter y for yes \n enter any key to exit :")

    if play_again.lower() == "y":
        play_game()
play_game()
