"""
Entry point for the Tic-Tac-Toe application.
"""

from inputs import read_human_player_mark
from samples import create_empty_board
from helper import get_opposite_mark
from models import Human, AI
from game import Frontier

def main():
    """
    Main function to prepare and begin the game.
    """

    initial_board = create_empty_board()

    human_mark = read_human_player_mark("Choose your mark (X or O): ")
    max_player = Human(human_mark)

    ai_mark = get_opposite_mark(human_mark)
    min_player = AI(ai_mark)

    frontier = Frontier(
        board=initial_board,
        max_player=max_player,
        min_player=min_player
    )

if __name__ == "__main__":
    main()
