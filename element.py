"""Base class and methods for use across elements of all apparatus.

Elements are movements defined by the FIG as individual skills of some set difficulty value.
"""


class Element:
    """Base class for elements across apparatus.
    
    Attributes:
        number (str): The box number assigned to an element in the COP.
    """
    def __init__(self, cop, number):
        self.cop = cop
        self.number = number
        self.description = None
        self.difficulty = None


class VTElement(Element):
    """Vault element."""
    def __init__(self, number):
        super().__init__(number)


class UBElement(Element):
    """Uneven bars element."""
    def __init__(self, number):
        super().__init__(number)


class BBElement(Element):
    """Balance beam element."""
    def __init__(self, number):
        super().__init__(number)


class FXElement(Element):
    """Floor exercise element."""
    def __init__(self, number):
        super().__init__(number)
