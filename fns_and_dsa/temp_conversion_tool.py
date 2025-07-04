FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
def convert_to_celcius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celcius):
    """Convert Celsius to Fahrenheit."""
    return (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
try:
    temperature =float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if  unit == 'F':
    converted_temp = convert_to_celcius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
elif unit == 'C':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")

    