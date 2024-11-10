"""
This package is responsible for managing every state of the Tic-Tac-Toe game.
"""

from models import Player, Board, Mark
from helpers import print_board
from .rules import is_board_full, winner_check

def start_game(max_player: Player, min_player: Player, board: Board) -> Mark:
    """
    This function is responsible for managing the states and the rules of the game.

    Args:
        max_player (Player): The player who wants to maximize the global score of the game.
        min_player (Player): The player who wants to minimize the global score of the game.
        board (Board): The board in which players will play on.

    Returns:
        Mark: The result of the game.

    Raises:
        ValueError: If the provided max_player object is not an instance of Player.
        ValueError: If the provided min_player object is not an instance of Player.
        ValueError: If the provided board object is not an instance of Board.
    """

    if not isinstance(max_player, Player):
        raise ValueError("Given max_player must be an instance of Player class.")

    if not isinstance(min_player, Player):
        raise ValueError("Given min_player must be an instance of Player class.")

    if not isinstance(board, Board):
        raise ValueError("Given board must be an instance of Board class.")

    result: Mark|None
    while not is_board_full(board):
        print_board(board)

        position = max_player.get_next_move(board)

        board.set_mark(
            row=position.get_row(),
            column=position.get_column(),
            mark=max_player.get_mark(),
        )

        result = winner_check(board)
        if result is not None:
            break

    print_board(board)

    return result
