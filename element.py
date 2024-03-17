"""Base class and methods for use across elements of all apparatus.

Elements are movements defined by the FIG as individual skills of some set difficulty value.
"""

from apparatus import Apparatus


class Element:
    """Base class for elements across apparatus.
    
    Attributes:
        number (str): The box number assigned to an element in the COP.
    """
    def __init__(self, number, cop=None, apparatus=None):
        self.number = number
        self.cop = cop.table[apparatus]
        self.apparatus = apparatus
        self.description = self.cop[self.cop['Number']]
        self.difficulty = None
    
    def get_difficulty(self, cop=None):
        self.cop = cop.table[self.apparatus] if cop else self.cop
        return self.cop[self.cop['Number'] == self.number]


class VTElement(Element):
    """Vault element."""
    def __init__(self, number, cop=None, apparatus=Apparatus.VT):
        super().__init__(number, cop, apparatus)


class UBElement(Element):
    """Uneven bars element."""
    def __init__(self, number, cop=None, apparatus=Apparatus.UB):
        super().__init__(number, cop, apparatus)


class BBElement(Element):
    """Balance beam element."""
    def __init__(self, number, cop=None, apparatus=Apparatus.BB):
        super().__init__(number, cop, apparatus)


class FXElement(Element):
    """Floor exercise element."""
    def __init__(self, number, cop=None, apparatus=Apparatus.FX):
        super().__init__(number, cop, apparatus)
