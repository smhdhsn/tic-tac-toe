"""
This module contains the functionalities for the game.
"""

from .rules import get_empty_cells, get_turn_mark
from .frontier import Frontier

# Expose methods at the package level.
__all__ = [
    'get_empty_cells',
    'get_turn_mark',
    'Frontier'
]
