"""
Entry point for the Tic-Tac-Toe application.
"""

from models import Board, Human, AI
from helpers import decide_marks
from game import Frontier

def main():
    """
    Main function to prepare and begin the game.
    """

    initial_board = Board()

    human_mark, ai_mark = decide_marks("Choose your mark (X or O): ")

    max_player = Human(human_mark)
    min_player = AI(ai_mark)

    frontier = Frontier(
        board=initial_board,
        max_player=max_player,
        min_player=min_player
    )

    frontier.board.print()

if __name__ == "__main__":
    main()
