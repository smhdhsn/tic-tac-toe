"""
Has the functions for representing a board on the /dev/stdout.
"""

from os import system, name as os_name
from models import Board


def print_board(board: Board) -> None:
    """
    Prints the board to the console.

    Raises:
        ValueError: If the provided object is not an instance of Board.
    """

    if not isinstance(board, Board):
        raise ValueError("Given board must be an instance of Board class.")

    _clear_screen()
    print(
        "     0   1   2  ",
        "   ┌───┬───┬───┐",
        f" 0 │ {board.get_mark(0, 0)} │ {board.get_mark(0, 1)} │ {board.get_mark(0, 2)} │",
        "   ├───┼───┼───┤",
        f" 1 │ {board.get_mark(1, 0)} │ {board.get_mark(1, 1)} │ {board.get_mark(1, 2)} │",
        "   ├───┼───┼───┤",
        f" 2 │ {board.get_mark(2, 0)} │ {board.get_mark(2, 1)} │ {board.get_mark(2, 2)} │",
        "   └───┴───┴───┘",
        sep="\n",
    )


def _clear_screen() -> None:
    """
    Clears the terminal screen.

    - On Windows, it uses the 'cls' command.
    - On macOS and Linux, it uses the 'clear' command.
    """

    system("cls" if os_name == "nt" else "clear")
