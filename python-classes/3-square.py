#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Defines a square and creates a private instance attribute """
    def __init__(self, size=0):
        """ initializes size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        square_area = self.__size ** 2
        return square_area
