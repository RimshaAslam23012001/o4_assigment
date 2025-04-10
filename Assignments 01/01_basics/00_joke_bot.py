prompt: str = "What do you want? "
joke_message: str = "Why did the chicken cross the road? To get to the other side!"
sorry: str = "Sorry, I can only tell you a joke."

def tell_joke():
    user_input: str = input(prompt)
    if user_input.lower() == "joke":
        print(joke_message)  # Now printing the string correctly
    else:
        print(sorry)

if __name__ == "__main__":
    tell_joke()
# The code now correctly prints the joke message when the user inputs "joke".