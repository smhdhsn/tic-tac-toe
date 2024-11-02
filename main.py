"""
Entry point for the Tic-Tac-Toe application.
"""

from samples import create_empty_board
from inputs import read_player_mark
from outputs import print_board
from models import Player

def main():
    """
    Main function to prepare and begin the game.
    """

    initial_state = create_empty_board()

    player_mark = read_player_mark("Choose your mark (X or O): ")

    max_player = Player(player_mark)

    initial_state.set_mark(1, 1, max_player.get_mark())

    print_board(initial_state)

if __name__ == "__main__":
    main()
