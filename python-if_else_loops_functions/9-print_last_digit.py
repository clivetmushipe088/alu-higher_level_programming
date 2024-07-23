#!/usr/bin/python3
def print_last_digit(number):
    # Get the last digit using modulo operation
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit

