# Constants
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

def mad_libs():
    # Prompt the user for an adjective, a noun, and a verb
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Construct and print the sentence using the input words
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

# Run the function when the script is executed
if __name__ == "__main__":
    mad_libs()
