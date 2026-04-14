"""
This package contains the frontier for the game application.
"""

from models import Board, Player

class Frontier:
    """
    A container for managing states and exploration of states.
    """

    def __init__(self, board: Board, max_player: Player, min_player: Player) -> None:
        """
        Initialize the Frontier with board and max player.

        Args:
            board (Board): The board of the Tic-Tac-Toe game.
            max_player (Player): The max player.
            min_player (Player): The min player.

        Raises:
            ValueError: If the provided board is not an instance of Board.
            ValueError: If the provided max_player is not an instance of Player.
            ValueError: If the provided min_player is not an instance of Player.
        """

        if not isinstance(board, Board):
            raise ValueError("Provided board has to be an instance of Board.")

        if not isinstance(max_player, Player):
            raise ValueError("Provided max player has to be an instance of Player.")

        if not isinstance(min_player, Player):
            raise ValueError("Provided min player has to be an instance of Player.")

        self.board: Board = board
        self.max_player: Player = max_player
        self.min_player: Player = min_player
