# Write a program to print terms in the Fibonacci sequence up to a maximum value.

max_value = 10000
def main():
    print("Fibonacci Sequence up to", max_value)
    a, b = 0, 1
    while a <= max_value:
        print(a, end=' ')
        a, b = b, a + b

if __name__ == "__main__":
    main()