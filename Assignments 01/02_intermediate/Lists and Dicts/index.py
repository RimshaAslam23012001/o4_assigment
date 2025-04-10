def access_element(lst, index):
    """Returns the element at the specified index or an error message if out of range."""
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range!"

def modify_element(lst, index, new_value):
    """Replaces the element at the specified index with a new value if index is valid."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element updated successfully!"
    return "Index out of range!"

def slice_list(lst, start, end):
    """Returns a sublist from start to end index, handling out-of-range cases."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst) and start < end:
        return lst[start:end]
    return "Invalid indices!"

def print_list(lst):
    """Prints the current state of the list."""
    print("\nCurrent List:", lst)

def main():
    # Initial list
    my_list = [10, "apple", 3.14, "banana", 42]

    print("\nWelcome to the List Manipulation Game!")
    print("-" * 50)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Access an element
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))

        elif choice == "2":
            # Modify an element
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))
        
        elif choice == "3":
            # Slice the list
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(my_list, start, end))
        
        elif choice == "4":
            # Exit the game
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
        
        # Display the updated list
        print_list(my_list)

if __name__ == "__main__":
    main()
# This code is a simple interactive program that allows users to manipulate a list.