# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    user_value = int(input("Enter a number: "))
    while user_value <= 100:
        user_value *= 2
        print("Doubled value:", user_value)
    print("Final value:", user_value)

if __name__ == "__main__":
    main()