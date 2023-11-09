#!/usr/bin/python3
def common_elements(set_1, set_2):
    element = {element for element in set_1 if element is in set_2}
