#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_lis):
        return my_list[idx]
    else:
        return my_list([idx],element)
