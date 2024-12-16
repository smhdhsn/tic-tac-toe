"""
This package contains the functions for getting inputs from user.
"""

from typing import Tuple
from beartype import beartype
from models import Mark


@beartype
def decide_marks(msg: str) -> Tuple[Mark, Mark]:
    """
    Decide human player's mark based on user input and assigns the opposite mark to the computer.

    Args:
        msg (str): The message to display to the user.

    Returns:
        Tuple[Mark, Mark]: A tuple containing the human player's mark and the computer's mark.

    Raises:
        ValueError: If the user's input is not 'X' or 'O'.
    """

    human_input = input(msg).strip().upper()
    human_mark = Mark(human_input)

    if human_mark not in {Mark.X, Mark.O}:
        raise ValueError("Please enter either 'X' or 'O'.")

    human_mark = Mark(human_input)
    ai_mark = Mark.O if human_mark == Mark.X else Mark.X

    return human_mark, ai_mark
