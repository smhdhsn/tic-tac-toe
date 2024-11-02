"""
This package defines the Mark enums, representing possible states of a cell in a Tic-Tac-Toe game.
"""

from enum import Enum

class Mark(Enum):
    """
    Enum for possible marks inside each cell in a Tic-Tac-Toe board.
    """

    EMPTY: str = ' '
    """
    The mark for an empty cell.
    """

    X: str = 'X'
    """
    A cell marked by player 'X'.
    """

    O: str = 'O'
    """
    A cell marked by player 'O'.
    """