"""
Module to create a board for the ticktacktoe game.
"""

from typing import List
from game import Mark

def create_empty_board() -> List[List[Mark]]:
    """
    Creates an empty board to initialize the game.

    Returns:
        List[List[Mark]]: The empty board as the initial state for the game.
    """

    return [
        [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
        [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
        [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY]
    ]
