import random

num_rounds = 5
score = 0

def main():
    global score  # Use the global score variable

    print("Welcome to the High-Low game!")
    print("-" * 50)

    for round_num in range(1, num_rounds + 1):
        my_random_number: int = random.randint(1, 100)
        computer_random_number: int = random.randint(1, 100)
        
        # Print the round number
        print(f"Round {round_num}")
        print("-" * 50)

        # Print the player's number for this round
        print(f"Your number is {my_random_number}")

        # Ask the user if they think their number is higher or lower
        user_guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Check if the user's guess is correct
        if (
            (user_guess == "higher" and my_random_number > computer_random_number)  # for higher
            or
            (user_guess == "lower" and my_random_number < computer_random_number)  # for lower
        ):
            print(f"You were right! The computer's number was {computer_random_number}.")
            score += 1  # Increment the score
            print(f"You got a point +1! Your score is now {score}.")
        else:
            print(f"You were wrong! The computer's number was {computer_random_number}.")

    # Print final score and feedback
    print(f"Your final score is {score} out of {num_rounds}.")
    print("Thanks for playing!")
    print("-" * 50)

    if score == num_rounds:
        print("Wow! You played perfectly!")
    elif score > num_rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
