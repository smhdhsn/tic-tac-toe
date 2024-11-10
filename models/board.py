"""
This module contains the Board class for managing a Tic-Tac-Toe game.
"""

from typing import List
import copy
from .mark import Mark


class Board:
    """
    This class is for managing the Tic-Tac-Toe game.
    """

    def __init__(self) -> None:
        """
        Initializes a 3x3 board with all cells set to EMPTY.
        """

        self.grid: List[List[Mark]] = [[Mark.EMPTY for _ in range(3)] for _ in range(3)]

    def get_grid(self) -> List[List[Mark]]:
        """
        Returns a copy of the board's grid.

        Returns:
            List[List[Mark]]: The grid inside the board.
        """

        return copy.deepcopy(self.grid)

    def set_mark(self, row: int, column: int, mark: Mark) -> None:
        """
        Sets a specified cell to a given mark.

        Args:
            column (int): The column index in the grid (0-2).
            row (int): The row index in the grid (0-2).
            mark (Mark): The mark to set in the specified cell.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= row < 3 and 0 <= column < 3):
            raise IndexError("Row and column indices must be between 0 and 2.")

        self.grid[row][column] = mark

    def get_mark(self, row: int, column: int) -> str:
        """
        Retrieves the mark inside a cell at a specified position in the grid.

        Args:
            column (int): The column index in the grid (0-2).
            row (int): The row index in the grid (0-2).

        Returns:
            str: The mark at the specified position.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= row < 3 and 0 <= column < 3):
            raise IndexError("Row and column indices must be between 0 and 2.")

        return self.grid[row][column].value

    def is_cell_empty(self, row: int, column: int) -> bool:
        """
        Checks if a cell at a specified position is empty.

        Args:
            row (int): The row index in the grid (0-2).
            column (int): The column index in the grid (0-2).

        Returns:
            bool: True if the cell is empty, False otherwise.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= column < 3 and 0 <= row < 3):
            raise IndexError("Column and row indices must be between 0 and 2.")

        return self.grid[row][column] == Mark.EMPTY
