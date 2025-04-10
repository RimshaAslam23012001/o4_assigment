# This program asks the user for their favorite animal and responds with the same animal.

def animal():
    # Prompt the user for their favorite animal and store the input as a string
    animal = str(input("What is your favourite animal? "))
    
    # Respond by printing a message that says the program's favorite animal is also the same
    print(f'My favourite animal is also {animal}!')

# This block ensures that the 'animal()' function is called when the script is executed directly
if __name__ == '__main__':
    animal()
