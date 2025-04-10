def main():
    user_value = int(input("Enter a number: "))
    while user_value <= 100:
        user_value *= 2
        print("Doubled value:", user_value)
    print("Final value:", user_value)

if __name__ == "__main__":
    main()