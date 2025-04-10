import random

DONE_LIKELIHOOD = 0.3  # Adjust the likelihood of stopping early

def done():
    return random.random() < DONE_LIKELIHOOD  # Returns True with DONE_LIKELIHOOD probability

def chaotic_counting():
    for i in range(1, 11):  # Count from 1 to 10
        if done():
            return  # Stop execution if done() returns True
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# Run the main function
main()