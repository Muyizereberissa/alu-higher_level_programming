#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is a valid string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Define the mapping of Roman numerals to integers
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    # Initialize the result
    result = 0

    # Iterate through the Roman string from left to right
    for i in range(len(roman_string)):
        # Get the integer value of the current Roman numeral
        value = roman_numerals[roman_string[i]]

        # If the value is less than the next value, subtract it; otherwise, add it
        if i < len(roman_string) - 1 and value < roman_numerals[roman_string[i + 1]]:
            result -= value
        else:
            result += value

    return result

