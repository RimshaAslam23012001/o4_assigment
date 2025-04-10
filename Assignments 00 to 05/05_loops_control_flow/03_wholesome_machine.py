# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly.

def main():
    affirmation = "I am capable of doing anything I put my mind to."
    user_input = input("Type the affirmation: ")

    while user_input != affirmation:
        print("Incorrect! Try again.")
        user_input = input("Type the affirmation: ")

    print("Correct! You are capable of doing anything you put your mind to.")

if __name__ == "__main__":
    main()
