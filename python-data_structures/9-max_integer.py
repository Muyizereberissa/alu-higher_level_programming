#!/usr/bin/python3
def max_integer(my_list=[]):
    big_num = my_list[0]
    for num in (len(my_list)):
        if num > big_num:
            big_num = num
    return big_num        
