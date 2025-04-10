# This program prompts the user to enter the lengths of the sides of a triangle and calculates its perimeter.

def main():
    print("Perimeter of a Triangle")
    side1 = float(input("Enter the length of side1: "))
    side2 = float(input("Enter the length of side2: "))
    side3 = float(input("Enter the length of side3: "))

    perimeter = side1 + side2 + side3
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()


    