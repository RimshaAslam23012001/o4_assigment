# This program converts a temperature from Fahrenheit to Celsius.

def temp():
   
    print("This is a program to convert Fahrenheit to Celsius.")

    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    
    # Convert the Fahrenheit temperature to Celsius using the formula: (Fahrenheit - 32) * 5/9
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    print(f'Temperature: {fahrenheit} F = {celsius} C')

# Ensure the temp() function is called when the script is executed directly
if __name__ == "__main__":
    temp()
