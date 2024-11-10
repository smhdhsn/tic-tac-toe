"""
This module contains the functionalities for the game.
"""

from .rules import get_empty_cells, get_turn_mark, is_board_full, winner_check
from .algorithm import start_game

# Expose methods at the package level.
__all__ = [
    'get_empty_cells',
    'get_turn_mark',
    'is_board_full',
    'winner_check',
    'start_game'
]
