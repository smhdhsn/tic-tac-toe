"""
This package contains the frontier for the game application.
"""

from models import Board, Player

class Frontier:
    """
    A container for managing states and exploration of states.
    """

    def __init__(self, board: Board, max_player: Player) -> None:
        """
        Initialize the Frontier with board and max player.

        Args:
            board (Board): The board of the tic-tac-toe game.
            max_player (Player): The max player.

        Raises:
            ValueError: If the provided board is not an instance of Board.
            ValueError: If the provided max_player is not an instance of Player.
        """

        self.board: Board = board
        self.max_player: Player = max_player
