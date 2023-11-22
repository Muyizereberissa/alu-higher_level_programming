#!/usr/bin/python3
""" Program that shows that object is exact the same """


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly an
    instance of the specified class ; otherwise False. """
    if (type(obj) == a_class):
        return True
    return False
