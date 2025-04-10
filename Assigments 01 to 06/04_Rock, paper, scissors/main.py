# rock paper scissors game
import random

print("Welcome to Rock, Paper, Scissors Game!")
print("-" * 40)
print("Game Rules:")
print("1. Rock crushes Scissors")
print("2. Scissors cuts Paper")
print("3. Paper covers Rock")
print("4. Type 'exit' to quit the game")
print("-" * 40)

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = computer_score = 0
    print("Let's play!")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
        if user_choice == 'exit':
            print("Thanks for Playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer Choose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            user_score += 1
            print("You win!")
        else:
            computer_score += 1
            print("Computer wins!")
        print(f"Score: You {user_score} - Computer {computer_score}")
        print("-" * 40)

    print(f"Final Score: You {user_score} - Computer {computer_score}")
    print("Thanks for playing!")
    print("-" * 40)
   
    print("Goodbye!")
    print("-" * 40)

if __name__ == "__main__":
    play_game()