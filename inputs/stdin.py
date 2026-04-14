"""
This package contains the functions for getting inputs from user.
"""

from models import Mark

def read_human_player_mark(msg: str) -> tuple:
    """
    Reads human player's mark from input.

    Raises:
        ValueError: If user's input is not 'X' or 'O'.

    Returns:
        str: User's mark.
    """
    s = Mark(input(msg).strip().upper())

    if s not in {Mark.X, Mark.O}:
        raise ValueError("Please enter either 'X' or 'O'.")

    return s
