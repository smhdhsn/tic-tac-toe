"""
Entry point for the Tic-Tac-Toe application.
"""

from samples import create_empty_board
from inputs import read_player_mark
from outputs import print_board

def main():
    """
    Main function to prepare and begin the game.
    """

    initial_state = create_empty_board()

    max_player = read_player_mark("Choose your marker (X or O): ")

    initial_state.set_cell(1, 1, max_player)

    print_board(initial_state)

if __name__ == "__main__":
    main()
