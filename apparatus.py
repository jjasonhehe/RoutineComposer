"""Apparatus class. Need to decide how to handle WAG vs MAG."""

from enum import Enum


class Apparatus(Enum):
    """Gymnastics apparatus."""
    VT = 'VT'
    UB = 'UB'
    BB = 'BB'
    FX = 'FX'
