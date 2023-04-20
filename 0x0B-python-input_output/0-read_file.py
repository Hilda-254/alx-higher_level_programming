#!/usr/bin/python3
"""Module reads a text file"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
