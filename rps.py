import random
def play_rock_paper_scissors():
    user_score = 0
    computer_score = 0
    while True:
        print("\nChoose one: (r)ock, (p)aper, (s)cissors, or (q)uit: ")
        user_choice = input().lower()

        if user_choice == 'q':
            break  

        if user_choice not in ['r', 'p', 's']:
            print("Invalid choice. Please choose r, p, s, or q.")
            continue  

        computer_choice = random.choice(['r', 'p', 's'])

        print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'r' and computer_choice == 's') or \
             (user_choice == 'p' and computer_choice == 'r') or \
             (user_choice == 's' and computer_choice == 'p'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Current scores: You {user_score}, Computer {computer_score}\n")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\nThanks for playing!")

play_rock_paper_scissors()
