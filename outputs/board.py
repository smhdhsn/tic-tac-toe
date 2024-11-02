"""
This module contains the function to print the game board to the console.
"""

from models import Board

def print_board(board: Board) -> None:
    """
    Prints the board to the console.

    Args:
        board (Board): The board to be printed.
    """

    print(
        "     0   1   2  ",
        "   ┌───┬───┬───┐",
        f" 0 │ {board.get_mark(0, 0)} │ {board.get_mark(1, 0)} │ {board.get_mark(2, 0)} │",
        "   ├───┼───┼───┤",
        f" 1 │ {board.get_mark(0, 1)} │ {board.get_mark(1, 1)} │ {board.get_mark(2, 1)} │",
        "   ├───┼───┼───┤",
        f" 2 │ {board.get_mark(0, 2)} │ {board.get_mark(1, 2)} │ {board.get_mark(2, 2)} │",
        "   └───┴───┴───┘",
        sep="\n"
    )
