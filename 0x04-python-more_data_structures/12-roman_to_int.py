#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_map = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }

    result = 0
    i = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1 and roman_string[i:i+2] in roman_to_int_map:
            result += roman_to_int_map[roman_string[i:i+2]]
            i += 2
        else:
            result += roman_to_int_map[roman_string[i]]
            i += 1

    return result
