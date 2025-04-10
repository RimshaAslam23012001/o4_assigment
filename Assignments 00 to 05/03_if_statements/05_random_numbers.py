# Print 10 random numbers in the range 1 to 100.

import random
def print_random_numbers():
    for _ in range(10):
        print(random.randint(1, 100))

if __name__ == "__main__":
    print_random_numbers()

