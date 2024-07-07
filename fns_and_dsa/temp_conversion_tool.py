CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5



# def convert_to_celsius(fahrenheit):
#     global FAHRENHEIT_TO_CELSIUS_FACTOR
#     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# def convert_to_fahrenheit(celsius):
#     global CELSIUS_TO_FAHRENHEIT_FACTOR
#     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# if __name__ == "__main__":
#     temp = input("Enter the temperature to convert: ")
#     try:
#         temp_case = input(
#             "Is this temperature in Celsius or Fahrenheit? (C/F): "
#         ).upper()
#         if temp_case == "F":
#             print(f"{temp}°F is {convert_to_celsius(float(temp))}°C")
#         elif temp_case == "C":
#             print(f"{temp}°C is {convert_to_fahrenheit(float(temp))}°F")
#     except ValueError as e:
#         print("Invalid temperature. Please enter a numeric value.")
