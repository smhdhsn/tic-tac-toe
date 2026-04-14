"""
This module contains the Board class for managing a Tic-Tac-Toe game.
"""

from typing import List
from .mark import Mark

class Board:
    """
    This class is for managing the Tic-Tac-Toe game.
    """

    def __init__(self) -> None:
        """
        Initializes a 3x3 board with all cells set to EMPTY.
        """

        self.grid: List[List[Mark]] = [
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY]
        ]

    def set_mark(self, column: int, row: int, mark: Mark) -> None:
        """
        Sets a specified cell to a given value.

        Args:
            row (int): The row index in the grid (0-2).
            column (int): The column index in the grid (0-2).
            mark (Mark): The mark inside a cell in a specified position of the board.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= row < 3 and 0 <= column < 3):
            raise IndexError("Row and column indices must be between 0 and 2.")

        self.grid[column][row] = mark

    def get_mark(self, column: int, row: int) -> str:
        """
        Retrieves the mark inside a cell at a specified position in the grid.

        Args:
            row (int): The row index in the grid (0-2).
            column (int): The column index in the grid (0-2).

        Returns:
            str: The value of a cell in a given position on the grid.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= row < 3 and 0 <= column < 3):
            raise IndexError("Row and column indices must be between 0 and 2.")

        return self.grid[column][row].value
