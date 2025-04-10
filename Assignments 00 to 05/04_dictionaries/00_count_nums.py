def count_numbers():
    count_dict = {}

    while True:
        user_input = input("Enter a number (or exit to stop): ").strip()  # Get input as a string

        if user_input.lower() == 'exit':  # Check for exit condition
            break
        
        # Attempt to convert the input to an integer
        try:
            num = int(user_input)
            count_dict[num] = count_dict.get(num, 0) + 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 'Exit'.")

    return count_dict

def print_counts(count_dict):
    print("\nNumber counts:")
    for key, value in count_dict.items():
        print(f"{key} appears {value} times.")

if __name__ == "__main__":
    count_dict = count_numbers()
    print_counts(count_dict)
