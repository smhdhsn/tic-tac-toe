"""
This package is the ai player in the game.
"""

from pickle import load
from dto import Position
from search import StateSpace, Frontier, min_value
from models import Player, Board, State, Mark


class Agent(Player):
    """
    This class holds the functionalities for the ai player in the Tic-Tac-Toe game.
    """

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

    def get_next_move(self, board: Board) -> Position:
        """
        Gets the next move of this player in a given board.

        Args:
            board (Board): The board in which the player has to make their next move.

        Returns:
            Position: The position in the board where the player wants to make their next move.
        """

        self._update_current_state(board)

        best_value: float = float("inf")
        best_state: State = None
        for state in self.current_state.get_next_states():
            score = min_value(state, Mark.X if self.get_mark() == Mark.O else Mark.O)
            if score < best_value:
                best_value = score
                best_state = state

        best_move = self._compare_boards(board, best_state.get_value())

        return best_move

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
