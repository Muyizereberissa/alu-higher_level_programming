#!/usr/bin/python3
for  i in range(0, 6):
    for j in range (0, 6):
        print("str(i)+str(j)".format(str), end=" "
                if str(i) < str(j):
                   print(str(i))
                else:
                   print(str(j))
