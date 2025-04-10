# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

def evens():
    print("The first 20 even numbers are:")
    for i in range(0, 40, 2):  # Start from 0, go up to 40 (exclusive), step by 2
        print(i, end=' ')
    print()  # Print a newline at the end

if __name__ == "__main__":
    evens()