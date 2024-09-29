FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
degree_symbol = "\u00B0"

def convert_to_celsius(fahrenheit):
    """"Converts Fahrenheit to Celcius using the value from user input in user prompt function"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius):
    """Converts Celcius to Fahrenheit using the value from user input in user prompt function"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


"""Line 14 to 21 is to recieve input from the user(temperature value) and validate it.
I chose not to use the try and except block just in case"""
temperature_value = (input('Enter the temperature to convert: '))
if temperature_value.isdigit():
    temperature_value = int(temperature_value)
else:
    print('Invalid temperature. Please enter a numeric value.')
    temperature_value = None

"""Line 23 to 36 is to recieve input from the user(temperature type) and validate it.
This will determine which of the functions will be run based on the input
It also contains a nested match and case to run the appropriate convertor based on the temperature type."""
temperature_type = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()
if temperature_type.isalpha():
    match temperature_type:
        case 'C':
            result = convert_to_fahrenheit(temperature_value)
            print(f'{temperature_value}{degree_symbol}{temperature_type} is {result:.13f}{degree_symbol}F')
        case 'F':
            result = convert_to_celsius(temperature_value)
            print(f'{temperature_value}{degree_symbol}{temperature_type} is {result:.13f}{degree_symbol}C')           
        case _:
            print("Did you mean 'C' for celcius or 'F' for fahrenheit? \nTry again")
else:
    print('Invalid Input, try letter of the alphabet.')
    temperature_type = None





     


