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

        self.grid: List[List[Mark]] = [[Mark.EMPTY for _ in range(3)] for _ in range(3)]

    def set_mark(self, column: int, row: int, mark: Mark) -> None:
        """
        Sets a specified cell to a given mark.

        Args:
            row (int): The row index in the grid (0-2).
            column (int): The column index in the grid (0-2).
            mark (Mark): The mark to set in the specified cell.

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
            str: The mark at the specified position.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= row < 3 and 0 <= column < 3):
            raise IndexError("Row and column indices must be between 0 and 2.")

        return self.grid[column][row].value

    def is_cell_empty(self, column: int, row: int) -> bool:
        """
        Checks if a cell at a specified position is empty.

        Args:
            column (int): The column index in the grid (0-2).
            row (int): The row index in the grid (0-2).

        Returns:
            bool: True if the cell is empty, False otherwise.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= column < 3 and 0 <= row < 3):
            raise IndexError("Column and row indices must be between 0 and 2.")

        return self.grid[column][row] == Mark.EMPTY

    def print(self) -> None:
        """
        Prints the board to the console.
        """

        print(
            "     0   1   2  ",
            "   ┌───┬───┬───┐",
            f" 0 │ {self.get_mark(0, 0)} │ {self.get_mark(1, 0)} │ {self.get_mark(2, 0)} │",
            "   ├───┼───┼───┤",
            f" 1 │ {self.get_mark(0, 1)} │ {self.get_mark(1, 1)} │ {self.get_mark(2, 1)} │",
            "   ├───┼───┼───┤",
            f" 2 │ {self.get_mark(0, 2)} │ {self.get_mark(1, 2)} │ {self.get_mark(2, 2)} │",
            "   └───┴───┴───┘",
            sep="\n"
        )
