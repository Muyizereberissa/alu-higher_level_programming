#!/usr/bin/python3
"""there is no module"""


class Square:
    """thi is a square class"""
    def __init__(self, size=0):
        self.__size = size  # private instance attribute

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
