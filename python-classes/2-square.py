#!/usr/bin/python3
"""there is no module available"""
class Square:
    """this is a square class"""
    def __init__(self, size=0):
        """this initializes an atribute to the object"""
        self.__size = size
try:
    print("{:d}".format(size))

except (TypeError):
    print("size must be an integer")
try:
    if size < 0:
    
    except (ValueError):
        print("size must be >= 0")
