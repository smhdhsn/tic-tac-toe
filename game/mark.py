"""
This package defines the Mark enums, representing possible states of a cell in a tic-tac-toe game.
"""

from enum import Enum

class Mark(Enum):
    """
    Enum for possible cell states in a tic-tac-toe game.
    """

    EMPTY: str = ' '
    """
    The mark for an empty cell.
    """

    X: str = 'X'
    """
    The mark of a cell chosen by player 'X'.
    """

    O: str = 'O'
    """
    The mark of a cell chosen by player 'O'.
    """
