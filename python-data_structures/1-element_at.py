#!/usr/bin/python3
def element_at(my_list, idx):
    for i in idx:
        if i < 0 and i != range(my_list):
            print(None)

        else:
            print(my_list, idx)

