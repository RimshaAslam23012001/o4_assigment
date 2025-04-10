# Define the legal adult age in the U.S.
ADULT_AGE = 18  

def is_adult(age):
    """
    Returns True if age is greater than or equal to ADULT_AGE, otherwise returns False.
    """
    return age >= ADULT_AGE  # Check if the age is 18 or older

def main():
    age = int(input("How old is this person?: "))  # Get user input and convert to integer
    print(is_adult(age))  # Call function and print the result

if __name__ == '__main__':
    main()