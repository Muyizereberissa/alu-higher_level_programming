#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''

class BaseGeometry:
    """thi is a class of geometry"""
    def area(self):
        """
        Calculate the area (not implemented in the base class).
        """
        raise NotImplementedError("area() method not implemented")

    def integer_validator(self, name, value):
        """
        Validate that the given value is a positive integer.

        :param name: The name of the value (used in error messages).
        :param value: The value to be validated.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
