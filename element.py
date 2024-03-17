"""Base class and methods for use across elements of all apparatus.

Elements are movements defined by the FIG as individual skills of some set difficulty value.
"""


class Element:
    """Base class for elements across apparatus.
    
    Args:
        number (str): The box number assigned to an element in the COP.
    """
    def __init__(self, number):
        self.number = number
        self.description = None
        self.difficulty = None
