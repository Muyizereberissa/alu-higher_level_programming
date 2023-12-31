#!/usr/bin/python3
"""this program sorts a list"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    It provides additional functionality to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        :return: None
        """
        sorted_list = sorted(self)
        print(sorted_list)
