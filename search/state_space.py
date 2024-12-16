"""
This package is responsible for creating the state space of the Tic-Tac-Toe game.
"""

from typing import Dict
from beartype import beartype
from models import Board, State, Mark
from game import get_empty_cells, winner_check, get_turn_mark


class StateSpace:
    """
    A class for managing the creation of a state space.
    """

    def __init__(self) -> None:
        """
        Initializes the creation of state space class.
        """

        self.visited_states: Dict[str, State] = {}

    @beartype
    def create(self, state: State, mark: Mark) -> None:
        """
        Creates state space of the game.

        Args:
            state (State): The state to begin creating the state space from.
            mark (Mark): The mark of the player in the turn.

        Raises:
            ValueError: If the given mark is neither 'X' or 'O'.
        """

        if mark is Mark.EMPTY:
            raise ValueError("The given mark has to be either 'X' or 'O'.")

        if winner_check(state.get_value()) is not None:
            return

        if get_turn_mark(state.get_value()) is not mark:
            return

        grid_hash = self.get_hash(state, mark)
        if grid_hash in self.visited_states:
            existing_state: State = self.visited_states[grid_hash]
            state.next_states = existing_state.get_next_states()
            return

        self.visited_states[grid_hash] = state

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
                    board,
                    parent_state=state,
                )
            )

        for next_state in state.get_next_states():
            self.create(
                state=next_state,
                mark=Mark.O if mark == Mark.X else Mark.X,
            )

    @beartype
    def get_hash(self, state: State, mark: Mark) -> str:
        """
        This function is responsible for getting the state's inner grid's string representation and
        adding the mark of the player in the turn at the very begining of it to create a unique key
        for the grid.

        Returns:
            str: Player's mark + string representation of the grid inside of the current state.

        Raises:
            ValueError: If the given mark is neither 'X' or 'O'.
        """

        if mark is Mark.EMPTY:
            raise ValueError("The given mark has to be either 'X' or 'O'.")

        return mark.value + state.get_content_hash()
