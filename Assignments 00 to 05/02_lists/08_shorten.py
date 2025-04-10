#Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 

MAX_LENGTH = 3
def shorten(lst):
    while len(lst)> MAX_LENGTH:
        last_element = lst.pop()
        print(last_element)

def get_list():
    lst =[]
    element:str = input("Enter an element to add in list: ")
    while element != "":
        lst.append(element)
        element = input("Enter an element to add in list: ")
    return lst

def main():
    lst = get_list()
    shorten(lst)
    print("The shortened list is:", lst)

if __name__ == "__main__":
    main()

