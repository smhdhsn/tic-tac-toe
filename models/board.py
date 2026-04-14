"""
This module contains the Board class for managing a Tic-Tac-Toe game.
"""

from typing import List
from .cell import Cell

class Board:
    """
    This class is for managing the Tic-Tac-Toe game.
    """

    def __init__(self) -> None:
        """
        Initializes a 3x3 board with all cells set to EMPTY.
        """

        self.grid: List[List[Cell]] = [
            [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
            [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
            [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY]
        ]

    def set_cell(self, column: int, row: int, cell: Cell) -> None:
        """
        Sets the specified cell to a given value.

        Args:
            row (int): The row index in the grid (0-2).
            column (int): The column index in the grid (0-2).
            cell (Cell): The Cell instance to place in the specified position.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= row < 3 and 0 <= column < 3):
            raise IndexError("Row and column indices must be between 0 and 2.")

        self.grid[column][row] = cell

    def get_cell(self, column: int, row: int) -> str:
        """
        Retrieves the cell at a specified position in the grid.

        Args:
            row (int): The row index in the grid (0-2).
            column (int): The column index in the grid (0-2).

        Returns:
            str: The value of a cell in a given position.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        if not (0 <= row < 3 and 0 <= column < 3):
            raise IndexError("Row and column indices must be between 0 and 2.")

        return self.grid[column][row].value
