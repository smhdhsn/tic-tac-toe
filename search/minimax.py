"""
This module holds functions for the operations related to minimax algorithm.
"""

from beartype import beartype
from models import State, Mark
from game import utility


@beartype
def max_value(state: State) -> float:
    """
    Computes the maximum utility value from the given state.

    Args:
        state (State): The current state of the game.

    Returns:
        float: Maximum utility achievable from this state.
    """

    score = utility(state.get_value(), Mark.X, is_max_player=True)
    if score is not None:
        return float(score)

    value = float("-inf")
    for next_state in state.get_next_states():
        value = max(
            value,
            min_value(next_state),
        )

    return value


@beartype
def min_value(state: State) -> float:
    """
    Computes the minimum utility value from the given state.

    Args:
        state (State): The current state of the game.

    Returns:
        float: Minimum utility achievable from this state.
    """

    score = utility(state.get_value(), Mark.O, is_max_player=False)
    if score is not None:
        return float(score)

    value = float("inf")
    for next_state in state.get_next_states():
        value = min(
            value,
            max_value(next_state),
        )

    return value
