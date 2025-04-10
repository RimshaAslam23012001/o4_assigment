# This program calculates the energy equivalent of a given mass using Einstein's formula: E = m * c^2

# Define the constant for the speed of light in meters per second
C = 299792458  # speed of light in meters per second

def calculate_energy():
    while True:
        try:
            # Ask the user to input the mass in kilograms
            mass = float(input("Enter kilos of mass: "))
            
            # Calculate the energy using the formula E = m * c^2
            energy = mass * C**2
            
            # Display the formula, mass, and the corresponding energy
            print(f"\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"E ={energy} joules")
            
        except ValueError:
            # Handle invalid input (non-numeric values)
            print("Please enter a valid number for the mass.")
        
        # Optionally, break the loop or continue reading user input
        continue_input = input("\nWould you like to enter another mass? (y/n): ").strip().lower()
        if continue_input != 'y':
            print("Goodbye!")
            break

# Run the function to start the program
if __name__ == "__main__":
    calculate_energy()
