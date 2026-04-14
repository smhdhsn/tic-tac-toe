"""
This package is responsible for creating the state space of the Tic-Tac-Toe game.
"""

from models import Board, State, Mark
from game import get_empty_cells


def create_state_space(state: State, mark: Mark):
    """
    Creates state space of the game.

    Args:
        state (State): The state to begin creating the state space from.
        mark (Mark): The mark of the player in the turn.

    Raises:
        ValueError: If the given state is not an instance of State class.
        ValueError: If the given mark is not an instance of Mark class.
        ValueError: If the given mark is neither 'X' or 'O'.
    """

    if not isinstance(state, State):
        raise ValueError("The given state is not an instance of State class.")

    if not isinstance(mark, Mark):
        raise ValueError("The given mark is not an instance of Mark class.")

    if mark is Mark.EMPTY:
        raise ValueError("The given mark has to be either 'X' or 'O'.")

    grid = state.get_content()
    positions = get_empty_cells(grid)

    for position in positions:
        board = Board(grid=grid)
        board.set_mark(
            position=position,
            mark=mark,
        )

        state.append_next_state(
            State(
                parent_state=state,
                content=board,
            )
        )

    for next_state in state.get_next_states():
        create_state_space(
            state=next_state,
            mark=Mark.O if mark == Mark.X else Mark.X,
        )
