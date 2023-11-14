#!/usr/bin/python3
"""there is no module available"""
class Square:
    """this is a square class"""
    def __init__(self, size=0):
        """this initializes an atribute to the object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
