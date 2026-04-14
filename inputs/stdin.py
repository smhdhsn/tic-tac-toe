"""
This package contains the functions for getting inputs from user.
"""

from game import Mark

def read_player_marker(msg: str) -> Mark:
    """
    Reads player's marker from input.

    Raises:
        ValueError: If user's input is not 'X' or 'O'.

    Returns:
        str: User's mark.
    """
    s = input(msg).strip().upper()

    if s not in {Mark.X.value, Mark.O.value}:
        raise ValueError("Please enter either 'X' or 'O'.")

    return Mark(s)
