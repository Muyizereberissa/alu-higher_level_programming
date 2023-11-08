#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    big_num = my_list[0]
    for num in my_list:
        if num > big_num:
            big_num = num
    return big_nuim
