# This program simulates rolling a pair of dice 1000 times and counts the number of times each total is rolled.
import random
def dice():
    die1:int = random.randint(1,6)
    die2:int = random.randint(1,6)
    total:int = die1 + die2

    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dices :", total)

if __name__ == "__main__":
    dice()
