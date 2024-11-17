"""
This module contains models and algorythms for the agent in the Tic-Tac-Toe game.
"""

from .explore import create_state_space

# Expose methods at the package level.
__all__ = ["create_state_space"]
