import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100, and the computer will guess it.")
print("You have to tell the computer if the guess is too high or too low.")

def guess_the_number():
    low = 1
    high = 100
    attempts = 0
    computer_guess = random.randint(low, high)
    attempts += 1
    feedback =''
    
    while feedback != 'c':
        print(f"Computer guesses: {computer_guess}")
        feedback = input("Enter 'h' if the guess is too high, 'l' if it's too low, and 'c' if it's corrrect: ").lower()

        if feedback == 'h':
            high = computer_guess -1
        elif feedback == 'l':
            low = computer_guess + 1
        elif feedback != 'c':
            print("Please enter a valid response: 'h', 'l', or 'c'.")
        else:
            print(f"Congratulations! Computer guessed the number {computer_guess} in {attempts} attempts.")
        computer_guess = random.randint(low, high)

    print("Thank you for playing!")


# Call the function to start the game
if __name__ == "__main__":
    guess_the_number()
