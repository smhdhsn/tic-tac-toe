"""
This package contains every game rule of the Tic-Tac-Toe game.
"""

from typing import List
from dto import Position
from models import Board, Mark

def get_turn_mark(board: Board) -> Mark:
    """
    Returns the mark that gets to play next on a given board.

    Returns:
        Mark: The mark of the player whose turn it is now.
    """

    x: int = 0
    o: int = 0

    for row in board.grid:
        for cell in row:
            if cell == Mark.X:
                x+=1
            elif cell == Mark.O:
                o+=1

    return Mark.X if x <= o else Mark.O

def get_empty_cells(board: Board) -> List[Position]:
    """
    Returns every available positions that can be taken on the board.

    Returns:
        List[Position]: The list of empty positions on the board.
    """

    available_positions: List[Position] = []

    for row_idx, row in enumerate(board.grid):
        for cell_idx, cell in enumerate(row):
            if cell == Mark.EMPTY:
                available_positions.append(Position(row=row_idx, column=cell_idx))

    return available_positions
