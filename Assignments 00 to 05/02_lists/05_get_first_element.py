#Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty.

def first_elemnt(list):
    print(list[0])

def get_list():
    list = []
    element:str = input("Enter an element to add in list: ")
    while element != "":
        list.append(element)
        element = input("Enter an element to add in list: ")
    return list
    
def main():
    list = get_list()
    first_elemnt(list)


if __name__ == "__main__":
    main()


