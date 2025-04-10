#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list.

def last_element(list):
    print(list[-1])

def get_list():
    list = []
    element:str = input("Enter an element to add in list: ")
    while element != "":
        list.append(element)
        element = input("Enter an element to add in list: ")
    return list
    
def main():
    list = get_list()
    last_element(list)


if __name__ == "__main__":
    main()
