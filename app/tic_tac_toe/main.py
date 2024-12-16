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

    player_a = Human(human_mark)
    player_b = Agent(agent_mark)

    result = run(
        player_a=player_a,
        player_b=player_b,
        board=board,
    )

    announce_result(result)


if __name__ == "__main__":
    main()
