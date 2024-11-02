"""
This package contains the functions for getting inputs from user.
"""

from models import Cell

def read_player_mark(msg: str) -> Cell:
    """
    Reads player's mark from input.

    Raises:
        ValueError: If user's input is not 'X' or 'O'.

    Returns:
        str: User's mark.
    """
    s = input(msg).strip().upper()

    if s not in {Cell.X.value, Cell.O.value}:
        raise ValueError("Please enter either 'X' or 'O'.")

    return Cell(s)
