#!/usr/bin/python3
'''function that reads a file UTF8'''


def read_file(filename=""):
    '''reads the data from outside file'''
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
