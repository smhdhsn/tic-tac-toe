"""
This package is the ai player in the game.
"""

from pickle import load
from search import StateSpace
from dto import Position
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
        self.state_space: State = None
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
