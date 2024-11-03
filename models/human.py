"""
This package is the human player in the game.
"""

from .player import Player
from .board import Board

class Human(Player):
    """
    This class holds the functionalities for the human player in the Tic-Tac-Toe game.
    """

    def get_next_move(self, board: Board) -> None:
        """
        Gets the next move of this player in a given board.

        Args:
            board (Board): The board in which the player has to make their next move.
        """
