def mad_libs():
    """Create a mad lib story by asking the user for various types of words."""
    print("Welcome to Mad libs!")
    print("Please enter the following words to create a mad lib story.")

    # Get user input for various types of words
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    funny_adjective = input("Enter a funny adjective: ")
    random_object = input("Enter a random object: ")
    bird = input("Enter a type of bird: ")
    action_verb = input("Enter an action verb: ")
    funny_exclamation = input("Enter a funny exclamation: ")
    noun = input("Enter a noun: ")

    story = (
        f"Once upon a time, {name} went to {place}. "
        f"They saw a {funny_adjective} {random_object} and decided to {action_verb} it. "
        f"Suddenly, a {bird} flew by and shouted '{funny_exclamation}!'. "
        f"{name} couldn't believe their eyes when they saw a giant {noun} appear out of nowhere!"
    )

    print("\nHere is your mad lib story:")
    print(story)

if __name__ == "__main__":
    mad_libs()