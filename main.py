"""
Entry point for the ticktacktoe application.
"""

from samples import create_empty_board
from outputs import print_board

def main():
    """
    Main function to prepare and begin the game.
    """

    initial_state = create_empty_board()

    print_board(initial_state)

if __name__ == "__main__":
    main()
