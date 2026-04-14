"""
This package contains the functions for announcing the result of the Tic-Tac-Toe game.
"""

from beartype import beartype
from models import Mark


@beartype
def announce_result(mark: Mark | None) -> None:
    """
    Announcing the result of the game.

    Args:
        mark (Mark): The mark of the winner player.
    """

    if mark is None:
        print("Game ended with a draw.")
    else:
        print(f"{mark.value} won the game!")
