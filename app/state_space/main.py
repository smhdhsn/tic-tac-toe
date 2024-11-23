"""
Entry point for calculating state space for the agent in the Tic-Tac-Toe application.
"""

from pickle import dump
from models import State, Board, Mark
from search import StateSpace


def main():
    """
    Main function to prepare and begin the calculation.
    """

    empty_board: Board = Board()
    initial_state: State = State(empty_board)

    for starting_player in [Mark.X, Mark.O]:
        StateSpace().create(
            initial_state,
            starting_player,
        )

    with open("export/state_space.pkl", "wb") as file:
        dump(initial_state, file)


if __name__ == "__main__":
    main()
