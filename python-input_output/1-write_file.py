#!/usr/bin/python3
'''script to write a string to a text file(UTF8) to return character num'''


def write_file(filename="", text=""):
    '''writes string to text file and returns characters number'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
