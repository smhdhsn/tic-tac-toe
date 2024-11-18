"""
Entry point for calculating state space for the agent in the Tic-Tac-Toe application.
"""

from pickle import dump
from models import State, Board, Mark
from search import create_state_space


def main():
    """
    Main function to prepare and begin the calculation.
    """

    default_mark: Mark = Mark.X
    empty_board: Board = Board()
    initial_state: State = State(empty_board)

    create_state_space(
        initial_state,
        default_mark,
    )

    with open("export/state_space.pkl", "wb") as file:
        dump(initial_state, file)


if __name__ == "__main__":
    main()
