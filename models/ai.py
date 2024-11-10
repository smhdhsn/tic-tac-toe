"""
This package is the ai player in the game.
"""

from dto import Position
from .player import Player
from .board import Board


class AI(Player):
    """
    This class holds the functionalities for the ai player in the Tic-Tac-Toe game.
    """

    def get_next_move(self, board: Board) -> Position:
        """
        Gets the next move of this player in a given board.

        Args:
            board (Board): The board in which the player has to make their next move.

        Returns:
            Position: The position in the board where the player wants to make their next move.
        """
