import random  # Import the random module to generate random numbers

# Function to simulate rolling two dice
def roll_dice():
    # Generate a random integer between 1 and 6 for the first die
    die1: int = random.randint(1, 6)  # generate random number for die1
    
    # Generate a random integer between 1 and 6 for the second die
    die2: int = random.randint(1, 6)  # generate random number for die2
    
    # Calculate the total of both dice
    total: int = die1 + die2
    
    # Print the result of the dice roll
    print(f'You rolled {die1} + {die2} = {total}')

# Main function where the program execution starts
def main():
    # Initialize die1 with the value 10 (this variable is not used in roll_dice)
    die1: int = 10
    # Print the value of die1 before calling roll_dice()
    print("die1 in main() starts as :" + str(die1))
    
    # Call the roll_dice function three times to simulate rolling the dice
    roll_dice()
    roll_dice()
    roll_dice()

    # Print the value of die1 after calling roll_dice() (it remains unchanged)
    print("die1 in main() is:" + str(die1))

# This condition ensures that the main() function is executed when the script is run directly
if __name__ == '__main__':
    main()
