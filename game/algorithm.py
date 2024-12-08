"""
This package is responsible for managing every state of the Tic-Tac-Toe game.
"""

from typing import Dict
from models import Player, Board, Mark
from views import print_board
from .rules import is_board_full, winner_check


def run(max_player: Player, min_player: Player, board: Board) -> Mark:
    """
    This function is responsible for managing the states and the rules of the game.

    Args:
        max_player (Player): The player who wants to maximize the global score of the game.
        min_player (Player): The player who wants to minimize the global score of the game.
        board (Board): The board in which players will play on.

    Returns:
        Mark: The result of the game.

    Raises:
        TypeError: If the provided max_player object is not an instance of Player.
        TypeError: If the provided min_player object is not an instance of Player.
        TypeError: If the provided board object is not an instance of Board.
    """

    if not isinstance(max_player, Player):
        raise TypeError("Given max_player must be an instance of Player class.")

    if not isinstance(min_player, Player):
        raise TypeError("Given min_player must be an instance of Player class.")

    if not isinstance(board, Board):
        raise TypeError("Given board must be an instance of Board class.")

    players: Dict[Mark:Player] = {
        max_player.get_mark(): max_player,
        min_player.get_mark(): min_player,
    }

    player: Player = players[Mark.X]
    result: Mark | None

    while not is_board_full(board):
        print_board(board)

        board.set_mark(
            position=player.get_next_move(board),
            mark=player.get_mark(),
        )

        result = winner_check(board)
        if result is not None:
            break

        player = players[Mark.X] if player.get_mark() == Mark.O else players[Mark.O]

    print_board(board)

    return result
