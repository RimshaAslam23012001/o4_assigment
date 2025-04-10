# This program asks the user for a number and prints its square.

def square():
    print('Square of a Number')
    number = int(input("Enter a number: "))   
    square = number ** 2
    print(f"The square of the number is {square}")

if __name__ == "__main__":
    square()


