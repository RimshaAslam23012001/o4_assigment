def print_multiple(message, repeats):
    """
    Prints the given message the specified number of times.
    """
    for _ in range(repeats):  # Loop repeats times
        print(message)  # Print the message

def main():
    message = input("Please type a message: ")  # Get user message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get repeat count
    print_multiple(message, repeats)  # Call the function

# Required line to execute the main function
if __name__ == '__main__':
    main()