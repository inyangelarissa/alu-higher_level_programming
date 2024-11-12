#!/usr/bin/python3
'''script that appends a string at the end of a text file'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file and returns charcters num'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
