"""
Entry point for the ticktacktoe application.
"""

from samples import create_empty_board
from inputs import read_player_marker
from outputs import print_board

def main():
    """
    Main function to prepare and begin the game.
    """

    initial_state = create_empty_board()

    max_player = read_player_marker("Choose your marker (X or O):")

    print_board(initial_state)

if __name__ == "__main__":
    main()
