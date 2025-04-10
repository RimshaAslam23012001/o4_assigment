def make_sentence(word, part_of_speech):
    """
    Prints a sentence using the given word based on its part of speech.
    """
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid input. Please enter 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    word = input("Please type a noun, verb, or adjective: ")  # Get the word
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))  # Get the part of speech
    make_sentence(word, part_of_speech)  # Call function to print the sentence

# Required line to execute the main function
if __name__ == '__main__':
    main()