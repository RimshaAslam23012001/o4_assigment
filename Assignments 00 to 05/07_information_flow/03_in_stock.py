# Assume Sophia's inventory is stored in a dictionary
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "grape": 15,
    "pear": 1000
}

def num_in_stock(fruit):
    """
    Returns the number of a given fruit in Sophia's inventory.
    If the fruit is not in stock, return 0.
    """
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").strip().lower()
    stock = num_in_stock(fruit)

    if stock > 0:
        print("\nThis fruit is in stock! Here is how many:\n")
        print(stock)
    else:
        print("\nThis fruit is not in stock.")

# Run the main function
if __name__ == '__main__':
    main()