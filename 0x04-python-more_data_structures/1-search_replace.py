#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Function that replaces all occurrences
    of an element by another in a new list
    """
    return [replace if element == search else element for element in my_list]
