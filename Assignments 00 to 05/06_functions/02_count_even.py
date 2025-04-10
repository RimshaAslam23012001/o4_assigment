def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = sum(1 for num in lst if num % 2 == 0)  # Count even numbers
    print(count)  # Print the count of even numbers

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Empty list to store integers
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop when user presses enter
            break
        try:
            lst.append(int(user_input))  # Convert input to integer and add to list
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return lst

def main():
    lst = get_list_of_ints()  # Get user input list
    count_even(lst)  # Count even numbers and print result

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()