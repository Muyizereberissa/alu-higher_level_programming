#!/usr/bin/python3 

def uppercase(str):
    str_2 = ""
    for i in str:

        if  ord(i) >= 97 and ord(i) <= 122:
            aux = chr(ord(i) - 32)
            str_2 += aux
        else:
            str_2 += i
    print(str_2)
