# #This program asks the user for lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
import math
def pythagorean_theorem():
    # Ask the user for the lengths of the two perpendicular sides of a right triangle
    ab = float(input("Enter the length of the first side: "))
    ac = float(input("Enter the length of the second side: "))

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    bc = float(math.sqrt(ab ** 2 + ac ** 2))

    # Output the length of the hypotenuse
    print(f"The length of the hypotenuse is {bc}")

if __name__ == "__main__":
    pythagorean_theorem()
    