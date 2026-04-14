"""
This module contains helper functions for mark.
"""

from models import Mark

def get_opposite_mark(mark: Mark) -> Mark:
    """
    Returns the opposite mark for a given mark.

    Args:
        mark (Mark): A mark to find the opposite mark based on.

    Returns:
        Mark: The opposite mark of a given mark.

    Raises:
        ValueError: If the given mark is neither 'X' or 'O'.
    """

    if mark not in {Mark.X, Mark.O}:
        raise ValueError("Given mark has to be either 'X' or 'O'.")

    return Mark.X if mark == Mark.O else Mark.O
