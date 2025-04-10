def main():
    for i in range(10, 20):  # Change range to start from 10 and go up to 19
        print(f"{i} {'odd' if is_odd(i) else 'even'}")

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    