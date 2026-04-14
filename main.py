"""
Entry point for the Tic-Tac-Toe application.
"""

from models import Board, Human, AI
from helpers import decide_marks

def main():
    """
    Main function to prepare and begin the game.
    """

    board = Board()

    human_mark, ai_mark = decide_marks("Choose your mark (X or O): ")

    max_player = Human(human_mark)
    min_player = AI(ai_mark)

    while True:
        board.print()

        position = max_player.get_next_move(board)

        board.set_mark(
            column=position.get_column(),
            row=position.get_row(),
            mark=max_player.get_mark(),
        )

if __name__ == "__main__":
    main()
