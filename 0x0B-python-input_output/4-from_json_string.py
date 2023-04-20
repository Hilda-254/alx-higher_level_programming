#!/usr/bin/python3
"""A function that returns an object (Python data structure)"""


import json


def from_json_string(my_str):
    """Returns a Python data structure"""
    return json.loads(my_str)
