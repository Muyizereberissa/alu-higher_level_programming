#!/usr/bin/python3
""" a module that imports sys"""

import sys
from your_module import save_to_json_file, load_from_json_file
"""documented"""

def add_items_to_list_and_save(arguments):
    """
    Adds all arguments to a Python list, then saves the list to a JSON file.

    Parameters:
    - arguments (list): List of arguments to be added to the Python list.

    Returns:
    - None
    """
    # Load existing list from file or create a new one
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    # Add new arguments to the list
    existing_list.extend(arguments)

    # Save the updated list to the file
    save_to_json_file(existing_list, 'add_item.json')

if __name__ == "__main__"
    arguments = sys.argv[1:]

    add_items_to_list_and_save(arguments)
