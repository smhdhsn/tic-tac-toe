"""
This module holds functions for the operations related to minimax algorithm.
"""

from beartype import beartype
from models import State, Mark
from game import utility


@beartype
def max_value(state: State, mark: Mark) -> float:
    """
    Computes the maximum utility value from the given state.

    Args:
        state (State): The current state of the game.
        mark (Mark): The maximizing player's mark.

    Returns:
        float: Maximum utility achievable from this state.
    """

    score = utility(state.get_value(), mark, is_max_player=True)
    if score is not None:
        return float(score)

    value = float("-inf")
    for next_state in state.get_next_states():
        value = max(
            value,
            min_value(next_state, _get_opponent_mark(mark)),
        )

    return value


@beartype
def min_value(state: State, mark: Mark) -> float:
    """
    Computes the minimum utility value from the given state.

    Args:
        state (State): The current state of the game.
        mark (Mark): The minimizing player's mark.

    Returns:
        float: Minimum utility achievable from this state.
    """

    score = utility(state.get_value(), mark, is_max_player=False)
    if score is not None:
        return float(score)

    value = float("inf")
    for next_state in state.get_next_states():
        value = min(
            value,
            max_value(next_state, _get_opponent_mark(mark)),
        )

    return value


def _get_opponent_mark(mark: Mark):
    """
    Returns the opponent's mark.

    Args:
        mark (Mark): The mark of the current player.

    Returns:
        Mark: The opponent of the given mark.
    """

    return Mark.X if mark == Mark.O else Mark.O
