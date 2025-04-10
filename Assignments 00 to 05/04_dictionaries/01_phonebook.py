# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def add_contact(phonebok):
    name = input(input("Enter the name of the contact: "))
    number = input("Enter the phone number of the contact: ")
    if name in phonebok:
        print(f"{name} Contact already exists.")
    else:
        phonebok[name] = number
        print(f"{name} added to the phonebook.")

def search_contact(phonebook):
    name = input("Enter the name of the contact you want to search for: ")
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}.")
    else:
        print(f"{name} not found in the phonebook.")

def display_contact(phonebook):
    if not phonebook:
        print("The phonebook is empty.")
    else:
        print("Phonebook contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")

def delete_contact(phonebook):
    name = input("Enter the name of the contact you want to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted from the phonebook.")
    else:
        print(f"{name} not found in the phonebook.")

def main():
    phonebook = {}
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            display_contact(phonebook)
        elif choice == '4':
            delete_contact(phonebook)
        elif choice == '5':
            print("Exiting the phonebook.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
