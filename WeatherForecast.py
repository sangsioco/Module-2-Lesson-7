# Task 1 Get temperature

def get_temperature():
    while True:
        temperature_str = input("Enter the temperature in Fahrenheit: ")
        try:
            temperature = float(temperature_str)
            return temperature
        except ValueError:
            print("Error: Please enter a numerical value for the temperature.")

temperature = get_temperature()
print("You entered:", temperature)

# Task 2 Temperature conversion

def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except Exception as e:
        print(f"An error occurred during the conversion: {e}")
        return None

fahrenheit_input = input("Enter the temperature in Fahrenheit: ")

try:
    fahrenheit = float(fahrenheit_input)
    celsius = fahrenheit_to_celsius(fahrenheit)
    if celsius is not None:
        print(f"The temperature in Celsius is: {celsius:.2f}°C")
except ValueError:
    print("Error: Please enter a numerical value for the temperature.")

# Task 3 User experience

finally:
    print("Thank you for using the weather forecast application!")
