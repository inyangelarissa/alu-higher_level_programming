#!/usr/bin/python3
def print_last_digit(number):
    ldigit = abs(number) % 10
    print(f"{ldigit}", end="")
    return ldigit
