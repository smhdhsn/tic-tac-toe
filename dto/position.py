"""
This package defines the position of a cell in the Tic-Tac-Toe game.
"""

class Position:
    """
    Represents a position on the board.
    """

    def __init__(self, row: int, column: int,):
        """
        Initializes the Position object.

        Args:
            column (int): The column of the position.
            row (int): The row of the position.

        Raises:
            IndexError: If the column or row is less than 0 or greater than 2.
        """

        if not (0 <= column < 3 and 0 <= row < 3):
            raise IndexError("Column and row indices must be between 0 and 2.")

        self.column: int = column
        self.row: int = row

    def get_column(self) -> int:
        """
        Returns the column of the position.

        Returns:
            int: The column of the position.
        """

        return self.column

    def get_row(self) -> int:
        """
        Returns the row of the position.

        Returns:
            int: The row of the position.
        """

        return self.row
