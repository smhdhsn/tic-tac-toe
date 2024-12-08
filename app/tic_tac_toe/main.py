"""
Entry point for the Tic-Tac-Toe application.
"""

from helpers import announce_result, decide_marks
from models import Board, Human, Agent
from game import run


def main():
    """
    Main function to prepare and begin the game.
    """

    board = Board()

    human_mark, agent_mark = decide_marks("Choose your mark (X or O): ")

    max_player = Human(human_mark)
    min_player = Agent(agent_mark)

    result = run(
        max_player=max_player,
        min_player=min_player,
        board=board,
    )

    announce_result(result)


if __name__ == "__main__":
    main()
