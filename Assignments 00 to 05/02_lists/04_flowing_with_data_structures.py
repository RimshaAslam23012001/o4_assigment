#add three copies of your message to a list
def add_three_copies(list,data):
    for i in range(3):
        list.append(data)

def main():
    message = input("Enter a message for copy: ")
    list = []
    print("Before adding copies: ", list)
    add_three_copies(list,message)
    print("After adding copies: ", list)

if __name__ == "__main__":
    main()
