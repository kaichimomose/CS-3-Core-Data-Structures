#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # decoded number
    number_base_10 = 0
    # for i in range(0, len(digits)):
    #     # TODO: Decode digits from binary (base 2)
    #     digit = digits[i]
    #     if base == 2:
    #         number_base_10 += base ** ((len(digits) - 1) - i) * int(digit)
    #     # TODO: Decode digits from hexadecimal (base 16)
    #     elif base == 16:
    #         if digit.isalpha():
    #             if digits.islower():
    #                 number_base_10 += base ** ((len(digits) - 1) - i) * (string.ascii_letters.index(digit) + 10)
    #             else:
    #                 number_base_10 += base ** ((len(digits) - 1) - i) * (string.ascii_letters.index(digit) + 10 - 26)
    #         else:
    #             number_base_10 += base ** ((len(digits) - 1) - i) * int(digits[i])
    # TODO: Decode digits from any base (2 up to 36)
    # iterate through each letter
    for i in range(0, len(digits)):
        # ith index letter
        digit = digits[i]
        # alphabet or digit
        if digit.isalpha():
            # lowercase or uppercase
            if digits.islower():
                # base number power of ((len(digits) - 1) - i) place value
                number_base_10 += base ** ((len(digits) - 1) - i) * (string.ascii_letters.index(digit) + 10)
            else:
                #
                number_base_10 += base ** ((len(digits) - 1) - i) * (string.ascii_letters.index(digit) + 10 - 26)
        else:
            #
            number_base_10 += base ** ((len(digits) - 1) - i) * int(digit)
    return number_base_10


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    encoded_number = ""
    # if base == 2:
    #     while number != 0:
    #         remainder = number % base
    #         encoded_number += str(remainder)
    #         number = round(number / base)
    # # TODO: Encode number in hexadecimal (base 16)
    # elif base == 16:
    #     while number != 0:
    #         remainder = number % base
    #         print(remainder)
    #         if remainder >= 10:
    #             remainder = string.ascii_letters[remainder - 10]
    #         encoded_number += str(remainder)
    #         # round down
    #         number = int(number / base)
    # TODO: Encode number in any base (2 up to 36)
    while number != 0:
        # calcurate remainder
        remainder = number % base
        if remainder >= 10:
            # get alphabet character
            remainder = string.ascii_letters[remainder - 10]
        # prepend remainder to encoded_number
        encoded_number = str(remainder) + encoded_number
        # round down
        number = int(number / base)
    return encoded_number


def decode_fractional_numbers(digits, base):
    """Decode given fractional numbers in given base to fractional numbers in base 10.
    digits: str -- string representation of fractional number (in given base)
    base: int -- base of given number
    return: float -- integer representation of fractional number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    integer_and_fractional_part = digits.split('.')

    integer = integer_and_fractional_part[0]
    fractional_part = integer_and_fractional_part[1]

    integer_number_base_10 = 0
    fractional_number_base_10 = 0

    for i in range(0, len(integer)):
        # ith index letter
        digit = integer[i]
        # alphabet or digit
        if digit.isalpha():
            # lowercase or uppercase
            if digits.islower():
                # base number power of ((len(digits) - 1) - i) place value
                integer_number_base_10 += base ** ((len(integer) - 1) - i) * (string.ascii_letters.index(digit) + 10)
            else:
                #
                integer_number_base_10 += base ** ((len(integer) - 1) - i) * (string.ascii_letters.index(digit) + 10 - 26)
        else:
            #
            integer_number_base_10 += base ** ((len(integer) - 1) - i) * int(digit)
    for i in range(0, len(fractional_part)):
        # ith index letter
        digit = fractional_part[i]
        print(digit)
        # alphabet or digit
        if digit.isalpha():
            # lowercase or uppercase
            if digits.islower():
                # base number power of (- 1 + i) place value
                fractional_number_base_10 += base ** (-(i + 1)) * (string.ascii_letters.index(digit) + 10)
            else:
                #
                fractional_number_base_10 += base ** (-(i + 1)) * (string.ascii_letters.index(digit) + 10 - 26)
        else:
            #
            fractional_number_base_10 += base ** (-(i + 1)) * int(digit)
    return str(integer_number_base_10 + fractional_number_base_10)


def encode_fractional_number(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    number = float(number)
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    integer = int(number)
    print(integer)
    fractional_part = number - integer
    print(fractional_part)
    encoded_number = ""
    while integer != 0:
        # calcurate remainder
        remainder = integer % base
        if remainder >= 10:
            # get alphabet character
            remainder = string.ascii_letters[remainder - 10]
        # prepend remainder to encoded_number
        encoded_number = str(remainder) + encoded_number
        # round down
        integer = int(integer / base)

    encoded_number += "."
    while fractional_part != 0:
        # calcurate remainder
        product = fractional_part * base
        integer = int(product)
        fractional_part = product - integer
        if integer >= 10:
            # get alphabet character
            integer = string.ascii_letters[integer - 10]
        # prepend remainder to encoded_number
        encoded_number += str(integer)
    return encoded_number


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    if '.' in digits:
        decoded_number = decode_fractional_numbers(digits, base1)
        encoded_number = encode_fractional_number(decoded_number, base2)
    else:
        decoded_number = decode(digits, base1)
        encoded_number = encode(decoded_number, base2)
    return encoded_number


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
