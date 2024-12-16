"""
This package is responsible for managing every state of the Tic-Tac-Toe game.
"""

from typing import Dict
from beartype import beartype
from models import Player, Board, Mark
from views import print_board
from .rules import is_board_full, winner_check


@beartype
def run(player_a: Player, player_b: Player, board: Board) -> Mark | None:
    """
    This function is responsible for managing the states and the rules of the game.

    Args:
        player_a (Player): Player a in the game.
        player_b (Player): Player b in the game.
        board (Board): The board in which players will play on.

    Returns:
        Mark: The result of the game.
    """

    players: Dict[Mark:Player] = {
        player_a.get_mark(): player_a,
        player_b.get_mark(): player_b,
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
