"""
Defines the State class representing nodes in the adversarial search space for the Tic-Tac-Toe game.
"""

from __future__ import annotations
from typing import List
from dto import Position
from .board import Board
from .mark import Mark


class State:
    """
    A representation of a state in the search space.
    """

    def __init__(self, parent_state: State | None, content: Board) -> None:
        """
        Initializes a node to hold and manage a state of the game.

        Args:
            parent_state (State | None): The state node that holds the parent of this state.
            board (Board): The content of this node.
        """

        self.parent_state: State = parent_state
        self.next_states: List[State] = []
        self.board: Board = content

    def append_next_state(self, state: State) -> None:
        """
        Appends a state to the list of next states.

        Args:
            state (State): The state to append.

        Raises:
            ValueError: If the provided state is not an instance of State class.
        """

        if not isinstance(state, State):
            raise ValueError("The provided state is not an instance of State class.")

        self.next_states.append(state)

    def get_next_states(self) -> List[State]:
        """
        Returns next states of this state.

        Returns:
            List[State]: A list of next states.
        """

        return self.next_states

    def action_to_here(self) -> Position:
        """
        The action that has happened to parent state that generated this state.

        Returns:
            Position: The cell that has been marked on parent state.

        Raises:
            ValueError: If current node doesn't have a parent node.
            ValueError: If current node and parent node are identical.
        """

        if self.parent_state is None:
            raise ValueError("This node doesn't have a parent node.")

        parent_grid = self.parent_state.get_content()
        curr_grid = self.get_content()

        for row_idx, row in enumerate(parent_grid):
            for cell_idx, parent_cell in enumerate(row):
                curr_cell = curr_grid[row_idx][cell_idx]

                if curr_cell != parent_cell:
                    return Position(
                        row=row_idx,
                        column=cell_idx,
                    )

        raise ValueError("Current node and parent node are identical.")

    def get_content(self) -> List[List[Mark]]:
        """
        Returns a copy of the content within this node.

        Returns:
            List[List[Mark]]: The grid representing board of the game.
        """

        return self.board.get_grid()

    def path_cost(self) -> int:
        """
        Calculates the path cost of reaching this state.

        Returns:
            int: The path cost to this state.
        """

        path_cost: int = 0
        state: State = self

        while state is not None:
            state = state.parent_state

            if state is not None:
                path_cost += 1

        return path_cost
