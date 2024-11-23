"""
This module contains the Board class for managing a Tic-Tac-Toe game.
"""

from typing import List
from copy import deepcopy
from dto import Position
from .mark import Mark


class Board:
    """
    This class is for managing the Tic-Tac-Toe game.
    """

    def __init__(self, grid: List[List[Mark]] | None = None) -> None:
        """
        Initializes a 3x3 board with all cells set to EMPTY.

        Args:
            grid (List[List[Mark]] | None): Initializes the Board with an optional grid.
        """

        if grid is not None:
            self.grid: List[List[Mark]] = deepcopy(grid)
        else:
            self.grid: List[List[Mark]] = [
                [Mark.EMPTY for _ in range(3)] for _ in range(3)
            ]

    def get_grid(self) -> List[List[Mark]]:
        """
        Returns a copy of the board's grid.

        Returns:
            List[List[Mark]]: The grid inside the board.
        """

        return deepcopy(self.grid)

    def get_grid_hash(self) -> str:
        """
        Returns string representation of the board which is in this node.

        Returns:
            str: The string representation of the grid.
        """

        grid = self.get_grid()

        return "".join("".join(cell.value for cell in row) for row in grid)

    def set_mark(self, position: Position, mark: Mark) -> None:
        """
        Sets a specified cell to a given mark.

        Args:
            position (Position): The position of a cell in the grid.
            mark (Mark): The mark to set in the specified cell.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        row = position.get_row()
        column = position.get_column()

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

    def is_cell_empty(self, position: Position) -> bool:
        """
        Checks if a cell at a specified position is empty.

        Args:
            position (Position): The position of a cell in the grid.

        Returns:
            bool: True if the cell is empty, False otherwise.

        Raises:
            IndexError: If the specified row or column is out of bounds.
        """

        row = position.get_row()
        column = position.get_column()

        if not (0 <= row < 3 and 0 <= column < 3):
            raise IndexError("Column and row indices must be between 0 and 2.")

        return self.grid[row][column] == Mark.EMPTY
