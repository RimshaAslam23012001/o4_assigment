# This program asks the user for two integers and performs division and remainder operations
def reminder():
    # Ask the user for two integers
    num1:int = int(input("Enter the first integer: "))
    num2:int = int(input("Enter the second integer: "))

    # Perform division and remainder operations
    quotient = num1 // num2
    remainder = num1 % num2

    # Display the results
    print(f"{num1} divided by {num2} is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    reminder()