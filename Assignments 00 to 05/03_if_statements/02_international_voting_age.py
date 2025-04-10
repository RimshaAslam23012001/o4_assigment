# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print("Your age is " + str(PETURKSBOUIPO_AGE) + "," " You can vote in Peturksbouipo." )
    else:
        print("Your age is " + str(PETURKSBOUIPO_AGE) + ","  " You cannot vote in Peturksbouipo.")
    
    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print("Your age is " + str(STANLAU_AGE) + ","  " You can vote in Stanlau.")
    else:
        print("Your age is " + str(STANLAU_AGE) + ","  " You cannot vote in Stanlau.")
    
    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print("Your age is " + str(MAYENGUA_AGE) + ","  " You can vote in Mayengua." )
    else:
        print("Your age is " + str(MAYENGUA_AGE) + ","  " You cannot vote in Mayengua.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()