"""
This package is the ai player in the game.
"""

from pickle import load
from beartype import beartype
from dto import Position
from search import StateSpace, Frontier, max_value, min_value
from models import Player, Board, State, Mark


class Agent(Player):
    """
    This class holds the functionalities for the ai player in the Tic-Tac-Toe game.
    """

    @beartype
    def __init__(self, mark: Mark) -> None:
        """
        Initializes the AI player with a specific mark and loads the state space.

        Args:
            mark (Mark): The mark assigned to the agent.
        """

        super().__init__(mark)
        self.current_state: State = None
        self.state_space: State = None
        self.frontier: Frontier = None
        self._load_state_space()

    def _load_state_space(self) -> None:
        """
        Loads the state space from a pickled file for the AI to reference during gameplay.

        Raises:
            FileNotFoundError: If the state space file is not found.
            Exception: If there is an error during the loading process.
        """

        if self.state_space is None:
            try:
                with open("export/state_space.pkl", "rb") as file:
                    self.state_space = load(file)

            except FileNotFoundError:
                initial_state = Board()
                initial_state: State = State(initial_state)

                StateSpace().create(
                    mark=self.get_mark(),
                    state=initial_state,
                )

                self.state_space = initial_state

    @beartype
    def get_next_move(self, board: Board) -> Position:
        """
        Gets the next move of this player in a given board.

        Args:
            board (Board): The board in which the player has to make their next move.

        Returns:
            Position: The position in the board where the player wants to make their next move.
        """

        self._update_current_state(board)

        best_state = self._get_best_state()
        best_move = self._compare_boards(board, best_state.get_value())

        return best_move

    @beartype
    def _get_best_state(self) -> State:
        """
        Determines the best next state for the agent based on its role as a player.

        Returns:
            State: The best next state for the agent according to the minimax strategy.
        """

        if self.get_mark().is_max_player():
            return self._play_as_maximizing_player()

        return self._play_as_minimizing_player()

    @beartype
    def _play_as_minimizing_player(self) -> State:
        """
        Finds the best next state assuming the agent is the minimizing player (O).

        This method iterates through all possible next states from the current state and
        uses the minimax algorithm's `min_value` function with O as the minimizing player.
        It chooses the state that results in the smallest utility value, thereby minimizing
        the opponent's advantage and optimizing the agent's outcome.

        Returns:
            State: The next state that yields the lowest utility value (best outcome for O).
        """

        best_value: float = float("inf")
        best_state: State = None
        for state in self.current_state.get_next_states():
            score = max_value(state)
            if score < best_value:
                best_value = score
                best_state = state

        return best_state

    @beartype
    def _play_as_maximizing_player(self) -> State:
        """
        Finds the best next state assuming the player is the maximizing player (X).

        This method iterates through all possible next states from the current state and
        uses the minimax algorithm's `max_value` function with X as the maximizing player.
        It selects the state that returns the greatest utility value, thereby maximizing the
        player's advantage.

        Returns:
            State: The next state that yields the highest utility value (best outcome for X).
        """

        best_value: float = float("-inf")
        best_state: State = None
        for state in self.current_state.get_next_states():
            score = min_value(state)
            if score > best_value:
                best_value = score
                best_state = state

        return best_state

    @beartype
    def _compare_boards(self, first: Board, second: Board) -> Position:
        """
        Finds the difference between two given grids.

        Args:
            first (Board): First board for comparison.
            second (Board): Second board for comparison.

        Returns:
            Position: The position of the cell that is different between two given grids.
        """

        first_grid = first.get_grid()
        second_grid = second.get_grid()

        for row_idx, row in enumerate(first_grid):
            for column_idx, cell in enumerate(row):
                if cell is not second_grid[row_idx][column_idx]:
                    return Position(
                        row=row_idx,
                        column=column_idx,
                    )

        return None

    @beartype
    def _update_current_state(self, board: Board) -> None:
        """
        Searches the state space to find the given board's corresponding state,
        allowing navigation within the state space. If found, updates the current state.

        Args:
            board (Board): The updated game state to locate in the state space.

        Raises:
            NotImplementedError: If the given board's state cannot be found.
        """

        if self.frontier is None:
            self.frontier = Frontier(self.state_space)

        while not self.frontier.is_empty():
            state = self.frontier.pop()

            if state.get_content_hash() == board.get_grid_hash():
                self.frontier.set_root(state)
                self.current_state = state
                return

            if not state.is_leaf():
                for next_state in state.get_next_states():
                    self.frontier.add(next_state)

        raise NotImplementedError(
            "Could not find the current state inside state space."
        )
