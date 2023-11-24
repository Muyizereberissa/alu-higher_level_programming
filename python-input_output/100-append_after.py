#!/usr/bin/python3
"""documented"""



def append_after(filename="", search_string="", new_string=""):
    """function documented"""
    if not filename:
        print("Please provide a filename.")
        return

    if not search_string:
        print("Please provide a search string.")
        return

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)

            if search_string in line:
                file.write(new_string + '\n')
