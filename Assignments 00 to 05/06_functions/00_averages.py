# Write a function that takes two numbers and finds the average between the two.
def find_average(num1, num2):
    return (num1 + num2) / 2

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

average = find_average(num1, num2)
print(f"The average of {num1} and {num2} is {average}")
