"""
Module to create a board for the Tic-Tac-Toe game.
"""

from models import Board

def create_empty_board() -> Board:
    """
    Creates an empty board to initialize the game.

    Returns:
        Board: The empty board as the initial state for the game.
    """

    return Board()
