# guess my numbers

import random

def guess_my_number():
    print("Welcome to the Guess My Number game!")
    print("I'm thinking of a number between 1 to 100.")
    
    # Generate a random number between 1 to 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_my_number()