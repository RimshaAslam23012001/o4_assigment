def greet(name):
    """
    Prints a greeting message with the given name.
    """
    print(f"Greetings {name}!")

def main():
    name = input("What's your name? ")  # Get user's name as input
    greet(name)  # Call the greet function with the user's name

if __name__ == '__main__':
    main()