"""
This package contains the functions for announcing the result of the Tic-Tac-Toe game.
"""

from models import Mark


def announce_result(mark: Mark) -> None:
    """
    Announcing the result of the game.

    Args:
        mark (Mark): The mark of the winner player.

    Raises:
        ValueError: If the provided object is not an instance of Mark.
    """

    if not isinstance(mark, Mark):
        raise ValueError("Given mark must be an instance of Mark class.")

    if mark == Mark.EMPTY:
        print("Game ended with a draw.")
    else:
        print(f"{mark.value} won the game!")
