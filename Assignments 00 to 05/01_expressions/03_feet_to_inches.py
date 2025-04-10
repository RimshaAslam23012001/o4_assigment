# asks user for feet and convert them into inches
inch: int = 12
def feet():
    feet: int = int(input("Enter the number of feet: "))
    inches: int = feet * inch
    print(f"{feet} feet is equal to {inches} inches")

if __name__ == "__main__":
    feet()