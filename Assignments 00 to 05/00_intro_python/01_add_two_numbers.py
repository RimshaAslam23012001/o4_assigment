# This program asks the user to enter two numbers and then adds them to gether

def add():
    print("This  program adds two numbers.")
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    total = int(num1 + num2)
    print("The total sum of", num1, "and", num2, "is", total)
# This block ensures that the 'animal()' function is called when the script is executed directly
if __name__ == '__main__':
    add()