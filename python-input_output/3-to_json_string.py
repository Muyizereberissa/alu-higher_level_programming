#!/usr/bin/python3
""" a JSON string-to-file function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)."""
    return json.dumps(my_obj)
