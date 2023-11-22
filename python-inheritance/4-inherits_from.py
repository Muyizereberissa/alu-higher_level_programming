#!/usr/bin/python3
"""Checks object class"""


def inherits_from(obj, a_class):
    """Checks object class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
