# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

minimum_height = 50

def height():
    height = int(input("How tall are you? "))
    if height >= minimum_height:
        print("You are tall enough to ride!")
    else:
        print("Sorry, you are not tall enough to ride.")

if __name__ == "__main__":
    height()
# This program asks the user for their height and checks if they are tall enough to ride a roller coaster.