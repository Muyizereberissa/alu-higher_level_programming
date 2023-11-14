#!/usr/bin/python3
"""there is no module available"""
class Square:
    """this is a square class"""
    def __init__(self, size=0):
        """this initializes an atribute to the object"""
        self.__size = size
        self.size = size
      @property
      def size(self):
      """getter value for the size attribute"""
      @size.setter 
      def size(self, value):
          """setter method for the attribute size
           value ; where the value to st must be an integer """
           if not isinstance(value, int):
               raise TypeError("size must be an integer")
           if value < 0:
               raise ValueError("size must be >= 0")

            self.__size = value       
