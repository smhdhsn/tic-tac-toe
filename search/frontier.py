"""
This module provides a simple abstraction for managing states to explore during graph searches.
"""

from collections import deque
from beartype import beartype
from models import State


class Frontier:
    """
    A generic frontier that can manage states to be explored.
    """

    @beartype
    def __init__(self, initial_state: State):
        """
        Initializes the frontier to manage exploration of state space.

        Args:
            initial_state (State): The state to start exploring from.
        """

        self._container: deque[State] = deque([initial_state])

    @beartype
    def add(self, state: State) -> None:
        """
        Add a state to the frontier.

        Args:
            state (State): The state to add to the frontier.
        """

        self._container.append(state)

    def pop(self) -> State:
        """
        Remove and return the next state from the frontier.

        Returns:
            State: The left most state in the queue.

        Raises:
            ValueError: If the frontier is empty.
        """

        if self.is_empty():
            raise ValueError("The frontier is empty.")

        return self._container.popleft()

    def is_empty(self) -> bool:
        """
        Check if the frontier is empty.

        Returns:
            bool: True if the frontier is empty, false otherwise.
        """

        return len(self._container) == 0

    @beartype
    def set_root(self, state: State) -> None:
        """
        Reset the frontier so that the given state is now the root state.
        This clears out the current frontier and starts fresh from this new state.

        Args:
            state (State): The state to set as the new root of the exploration.
        """

        self._container.clear()
        self._container.append(state)
