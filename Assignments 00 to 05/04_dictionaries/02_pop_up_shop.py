def fruit_cost():
    # Define the fruit prices
    fruit_prices = {
        "apple": 0.5,
        "banana": 0.25,
        "orange": 0.75,
        "grape": 0.1,
        "kiwi": 1.5
    }

    total_cost = 0

    # Loop through the dictionary and ask for user input
    for fruit, price in fruit_prices.items():
        while True:
            try:
                # Ask for the quantity of the selected fruit
                quantity = int(input(f"How many {fruit} would you like to buy? "))
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                # Accumulate the total cost
                total_cost += quantity * price
                print(f"The total cost for {quantity} {fruit}(s) is: ${quantity * price:.2f}")
                break  # Exit loop if valid quantity is entered
            except ValueError:
                print("Please enter a valid number.")
    
    # Print the total cost after all fruits
    print(f"\nThe total cost of your fruits is: ${total_cost:.2f}")

# Call the function to execute the program
if __name__ == "__main__":
    fruit_cost()
