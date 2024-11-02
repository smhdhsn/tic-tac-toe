"""
This module contains the function to print the game board to the console.
"""

from typing import List
from game import Mark

def print_board(board: List[List[Mark]]) -> None:
    """
    Prints the board to the console.

    Args:
        board (List[List[Mark]]): The board to be printed.
    """

    print(
        "     0   1   2  ",
        "   ┌───┬───┬───┐",
        f" 0 │ {board[0][0].value} │ {board[0][1].value} │ {board[0][2].value} │",
        "   ├───┼───┼───┤",
        f" 1 │ {board[1][0].value} │ {board[1][1].value} │ {board[1][2].value} │",
        "   ├───┼───┼───┤",
        f" 2 │ {board[2][0].value} │ {board[2][1].value} │ {board[2][2].value} │",
        "   └───┴───┴───┘",
        sep="\n"
    )
