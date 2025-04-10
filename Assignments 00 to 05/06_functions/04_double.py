def double(num):
    """
    Returns double the value of num.
    >>> double(2)
    4
    >>> double(5)
    10
    """
    return num * 2  # Multiply num by 2 and return the result

def main():
    num = int(input("Enter a number: "))  # Get user input and convert it to an integer
    result = double(num)  # Call the double function
    print(f"Double that is {result}")  # Print the result

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()