#Write a program which continuously asks the user to enter values which are added one by one into a list.

def main():
    lst = []
    val = input("Enter a value to add to the list (or 'done' to finish): ")
    while val:
        lst.append(val)
        val = input("Enter a value to add to the list (or 'done' to finish): ")
    print("The list is:", lst)

if __name__ == "__main__":
    main()
