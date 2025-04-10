# This program calculates and prints the ages of Anton, Beth, Chen, Drew, and Ethan based on given age relationships.
def ages():

    anthon:int = 21
    beth:int = anthon + 6
    chen:int = beth + 20
    drew:int = chen + anthon
    ethan:int = chen

    print(f"Anton is {anthon} years old.")
    print(f"Beth is {beth} years old.")
    print(f"Chen is {chen} years old.")
    print(f"Drew is {drew} years old.")
    print(f"Ethan is {ethan} years old.")
    
if __name__ == "__main__":
    ages()
