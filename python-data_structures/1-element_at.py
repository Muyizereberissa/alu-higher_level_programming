#!/usr/bin/python3
def element_at(my_list, idx):
    for i in idx:
        if i < 0 and i != range(my_list):
            return None

        else:
            return (my_list, idx)

