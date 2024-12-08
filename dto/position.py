"""
This package defines the position of a cell in the Tic-Tac-Toe game.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """
    Represents a position on the Tic-Tac-Toe board.
    Indices must be between 0 and 2 for both row and column.
    """

    row: int
    column: int

    def __post_init__(self):
        if not (0 <= self.row < 3 and 0 <= self.column < 3):
            raise ValueError("Row and column indices must be between 0 and 2.")
