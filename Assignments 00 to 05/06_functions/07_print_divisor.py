def print_divisors(num):
    """
    Prints all divisors of the given number.
    """
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):  # Iterate from 1 to num
        if num % i == 0:  # Check if i is a divisor
            print(i, end=" ")  # Print divisors on the same line

def main():
    num = int(input("Enter a number: "))  # Get user input
    print_divisors(num)  # Call the function

# Required line to execute the main function
if __name__ == '__main__':
    main()