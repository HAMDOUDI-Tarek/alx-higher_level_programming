#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Function that adds all unique
    integers in a list (only once for each integer)
    """
    return sum([num if num not in new_list for num in my_list])
