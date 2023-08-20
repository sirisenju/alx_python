# !/usr/bin/python3

class AlxClass:
    """
    This is an empty class.
    It serves as a placeholder and does nothing.
    """
    pass


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class; otherwise False.
    """
    return type(obj) is a_class

