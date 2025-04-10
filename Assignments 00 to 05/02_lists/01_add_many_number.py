#Write a function that takes a list of numbers and returns the sum of those numbers.

def add_number(numbers)->int:
    num = 0
    for i in numbers:
        num += i
    return num
# Test cases
def main():
    # case 1
    numbers:list[int] = [1, 2, 3, 4, 5]
    sum = add_number(numbers)
    print(f"Sum of {numbers} is {sum}")

    # case 2
    numbers = [-1, -2, -3, -4, -5]
    sum = add_number(numbers)
    print(f"Sum of {numbers} is {sum}")


if __name__ == "__main__":
    main()