def convert_temperature(temp, unit):
    if unit.lower() == 'c':
        # Convert Celsius to Fahrenheit and Kelvin
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        return fahrenheit, kelvin
    elif unit.lower() == 'f':
        # Convert Fahrenheit to Celsius and Kelvin
        celsius = (temp - 32) * 5/9
        kelvin = (temp - 32) * 5/9 + 273.15
        return celsius, kelvin
    elif unit.lower() == 'k':
        # Convert Kelvin to Celsius and Fahrenheit
        celsius = temp - 273.15
        fahrenheit = (temp - 273.15) * 9/5 + 32
        return celsius, fahrenheit
    else:
        return None

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")

    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the original unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ")

    result = convert_temperature(temp, unit)

    if result:
        if unit.lower() == 'c':
            print(f"{temp}°C is equal to {result[0]}°F and {result[1]}K")
        elif unit.lower() == 'f':
            print(f"{temp}°F is equal to {result[0]}°C and {result[1]}K")
        elif unit.lower() == 'k':
            print(f"{temp}K is equal to {result[0]}°C and {result[1]}°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

if __name__ == "_main_":
    main()