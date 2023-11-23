#!/usr/bin/python3
"""docemented"""


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file using the 'with' statement.

    Args:
        my_obj (object): The object to be saved to the JSON file.
        filename (str): The path to the JSON file.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
    """

    try:
        with open(filename, 'w+') as f:
            json.dump(my_obj, f, indent=4)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file '{filename}'")
