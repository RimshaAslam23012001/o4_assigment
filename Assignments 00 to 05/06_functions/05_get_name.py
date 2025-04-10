def get_name():
    """
    Returns the name as a string.
    """
    return "Jennat"  # The autograder expects "Jennat" to be returned

def main():
    name = get_name()  # Call get_name() to get the name
    print(f"Howdy {name} ! 🤠")  # Print the greeting

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()