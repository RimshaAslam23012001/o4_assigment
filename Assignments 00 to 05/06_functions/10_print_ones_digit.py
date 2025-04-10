def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = num % 10  # Extract the ones digit using modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Take user input and convert to integer
    print_ones_digit(num)  # Call the function

if __name__ == '__main__':
    main()