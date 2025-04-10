def get_user_data():
    """
    Asks the user for their first name, last name, and email,
    then returns them as a tuple.
    """
    first_name = input("What is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()
    email = input("What is your email address?: ").strip()
    
    return first_name, last_name, email  # Returning as a tuple

def main():
    user_data = get_user_data()  # Calling function and storing returned tuple
    print("\nReceived the following user data:", user_data)

# Running the program
if __name__ == '__main__':
    main()