#!/usr/bin/python3
"""
    empty class BaseGeometry
"""


class BaseGeometry:
    """ BaseGeometry class empty """

    def __dir__(self):
        """
        Get the list of attributes from the parent class (object class)
        """
        attributes = super().__dir__()

        """ Exclude __init_subclass__ from the list of attributes
        """
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
