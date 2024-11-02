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

    max_player = read_player_marker("Choose your marker (X or O): ")

    initial_state[0][0] = max_player
    initial_state[0][1] = max_player
    initial_state[0][2] = max_player

    initial_state[1][0] = max_player
    initial_state[1][1] = max_player
    initial_state[1][2] = max_player

    initial_state[2][0] = max_player
    initial_state[2][1] = max_player
    initial_state[2][2] = max_player

    print_board(initial_state)

if __name__ == "__main__":
    main()
