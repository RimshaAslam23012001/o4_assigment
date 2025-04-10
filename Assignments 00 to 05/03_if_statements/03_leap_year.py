# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

def leap_year():
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:

             print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    leap_year()
# The program checks if a year is a leap year or not.
