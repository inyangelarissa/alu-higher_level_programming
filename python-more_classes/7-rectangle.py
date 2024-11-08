#!/usr/bin/python3
""" Defines the rectangle """


class Rectangle:
    """DEfines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes the variables"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method to get the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to get the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        r_area = self.__width * self.__height
        return r_area

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        r_perimeter = 2 * (self.__width + self.__height)

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return r_perimeter

    def __del__(self):
        """Detects the deletion of an instance and returns bye when deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Prints the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rect = ''
            for i in range(self.__height):
                for x in range(self.__width):
                    rect = rect + str(self.print_symbol)

                rect += '\n'
            return rect[:-1]

    def __repr__(self):
        """Prints the string representation officially"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
