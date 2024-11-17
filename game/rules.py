"""
This package contains every game rule of the Tic-Tac-Toe game.
"""

from typing import List
from models import Board, Mark
from dto import Position


def get_turn_mark(board: Board) -> Mark:
    """
    Returns the mark that gets to play next on a given board.

    Returns:
        Mark: The mark of the player whose turn it is now.
    """

    x: int = 0
    o: int = 0

    for row in board.get_grid():
        for cell in row:
            if cell == Mark.X:
                x += 1
            elif cell == Mark.O:
                o += 1

    return Mark.X if x <= o else Mark.O


def get_empty_cells(grid: List[List[Mark]]) -> List[Position]:
    """
    Returns every available positions that can be taken on the board.

    Args:
        grid (List[List[Mark]]): The grid to search empty cells on.

    Returns:
        List[Position]: The list of empty positions on the board.
    """

    available_positions: List[Position] = []

    for row_idx, row in enumerate(grid):
        for cell_idx, cell in enumerate(row):
            if cell == Mark.EMPTY:
                available_positions.append(Position(row=row_idx, column=cell_idx))

    return available_positions


def winner_check(board: Board) -> Mark | None:
    """
    Checks if the game is over and returns the result accordingly.

    Args:
        board (Board): The board to check the result of the game on.

    Raises:
        ValueError: If the provided board object is not an instance of Board.
    """

    if not isinstance(board, Board):
        raise ValueError("Given board must be an instance of Board class.")

    grid = board.get_grid()

    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != Mark.EMPTY:
            return row[0]

    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != Mark.EMPTY:
            return grid[0][col]

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != Mark.EMPTY:
        return grid[0][0]

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != Mark.EMPTY:
        return grid[0][2]

    return None


def is_board_full(board: Board) -> bool:
    """
    Checks if the board has an empty cell.

    Args:
        board (Board): The board to check.

    Returns:
        bool: Weather the board has an empty cell or not.

    Raises:
        ValueError: If the provided board object is not an instance of Board.
    """

    if not isinstance(board, Board):
        raise ValueError("Given board must be an instance of Board class.")

    for row in board.get_grid():
        for cell in row:
            if cell == Mark.EMPTY:
                return False

    return True
