# Planetary Weights Calculator

def planetary_weight(earth_weight, planet):
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    if planet not in gravity_factors:
        return None
    return round(earth_weight * gravity_factors[planet], 2)

def main():
    try:
        earth_weight = float(input("Enter your weight on Earth: "))
        planet = input("Enter a planet: ").capitalize()

        planetary_weight_result = planetary_weight(earth_weight, planet)

        if planetary_weight_result is None:
            print("Invalid planet name. Please try again.")
        else:
            print(f"The equivalent weight on {planet}: {planetary_weight_result} lbs")
            if planetary_weight_result == earth_weight:
                print("Wow! Your weight remains the same!")
            elif planetary_weight_result > earth_weight:
                print("Whoa! You would weigh more on this planet!")
            else:
                print("Nice! You'd be lighter on this planet!")

    except ValueError:
        print("Invalid input! Please enter a valid weight.")

if __name__ == "__main__":
    main()

