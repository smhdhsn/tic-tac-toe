"""
This module contains the function to print the game board to the console.
"""

from typing import List

def print_board(board: List[List[str]]) -> None:
    """
    Prints the board to the console.

    Args:
        board (List[List[str]]): The board to be printed.
    """

    print(
        "┌───┬───┬───┐",
        "│ {} │ {} │ {} │".format(*board[0]),
        "├───┼───┼───┤",
        "│ {} │ {} │ {} │".format(*board[1]),
        "├───┼───┼───┤",
        "│ {} │ {} │ {} │".format(*board[2]),
        "└───┴───┴───┘",
        sep="\n"
    )
