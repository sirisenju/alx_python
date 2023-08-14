# !/usr/bin/python3

class Square:
    """A square class. This square class has a private attribute named size
    and it is a private attribute. Getters and setters has been put in place to obtain data from the user.
    """
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
    
    def set_size(self, size):
        self.__size = size

