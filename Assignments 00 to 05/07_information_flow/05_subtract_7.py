def subtract_seven(num):
    """
    Subtracts 7 from the given number and returns the result.
    """
    return num - 7  # Subtracting 7 from num

def main():
    number = int(input("Enter a number: "))  # Taking user input
    result = subtract_seven(number)  # Calling the helper function
    print("Result after subtracting 7:", result)  # Printing the result

# Running the program
if __name__ == '__main__':
    main()