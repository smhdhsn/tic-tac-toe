"""
Entry point for the Tic-Tac-Toe application.
"""

from models import Board, Human, AI
from helpers import announce_result, decide_marks
from game import start_game

def main():
    """
    Main function to prepare and begin the game.
    """

    board = Board()

    human_mark, ai_mark = decide_marks("Choose your mark (X or O): ")

    max_player = Human(human_mark)
    min_player = AI(ai_mark)

    result = start_game(
        max_player=max_player,
        min_player=min_player,
        board=board,
    )

    announce_result(result)

if __name__ == "__main__":
    main()
