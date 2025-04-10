import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct, too high, or too low
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
    print("Thank you for playing!")

if __name__ == "__main__":
    guess_the_number()