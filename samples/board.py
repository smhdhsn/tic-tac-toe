"""
Module to create a board for the ticktacktoe game.
"""

from typing import List

def create_empty_board() -> List[List[str]]:
    """
    Creates an empty board to initialize the game.

    Returns:
        List[List[str]]: The empty board as the initial state for the game.
    """

    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
