#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return ''
    return list(map(lambda x: {x + number}, my_list))
