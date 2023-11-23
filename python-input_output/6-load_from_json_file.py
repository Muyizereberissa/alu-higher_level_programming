#!/usr/bin/python3
"""this is a domentation"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Returns:
    - object: The object created from the JSON file.
    """
    with open(filename, 'r') as file:
        json_data = file.read()
        # Assuming the JSON file contains a valid JSON string
        loaded_object = json.loads(json_data)

    return loaded_object
