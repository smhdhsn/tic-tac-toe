"""
Has the functions for representing a board on the /dev/stdout.
"""

from models import Board

def print_board(board: Board) -> None:
    """
    Prints the board to the console.

    Raises:
        ValueError: If the provided object is not an instance of Board.
    """

    if not isinstance(board, Board):
        raise ValueError("Given board must be an instance of Board class.")

    print(
        "     0   1   2  ",
        "   ┌───┬───┬───┐",
        f" 0 │ {board.get_mark(0, 0)} │ {board.get_mark(0, 1)} │ {board.get_mark(0, 2)} │",
        "   ├───┼───┼───┤",
        f" 1 │ {board.get_mark(1, 0)} │ {board.get_mark(1, 1)} │ {board.get_mark(1, 2)} │",
        "   ├───┼───┼───┤",
        f" 2 │ {board.get_mark(2, 0)} │ {board.get_mark(2, 1)} │ {board.get_mark(2, 2)} │",
        "   └───┴───┴───┘",
        sep="\n"
    )
