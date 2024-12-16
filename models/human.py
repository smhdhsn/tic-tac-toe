"""
This package is the human player in the game.
"""

from sys import exit as sys_exit
from beartype import beartype
from dto import Position
from models import Player, Board


class Human(Player):
    """
    This class holds the functionalities for the human player in the Tic-Tac-Toe game.
    """

    @beartype
    def get_next_move(self, board: Board) -> Position:
        """
        Gets the next move of this player in a given board.

        Args:
            board (Board): The board in which the player has to make their next move.

        Returns:
            Position: The position in the board where the player wants to make their next move.
        """

        print("Please enter your next move:")

        while True:
            position = Position(
                row=self._get_position_from_input("Row:    "),
                column=self._get_position_from_input("Column: "),
            )

            try:
                if board.is_cell_empty(position):
                    break

                print("The cell is already occupied. Please try again.")

            except IndexError:
                print("Invalid position. Please try again.")

        return position

    @beartype
    def _get_position_from_input(self, msg: str) -> int:
        """
        Get the position from the user.

        Args:
            msg (str): The message to display to the user.

        Returns:
            str: A position on the board.
        """

        while True:
            try:
                user_input = input(msg).strip()
                position = int(user_input)

            except KeyboardInterrupt:
                sys_exit()

            except ValueError:
                print("Invalid position. Please try again.")
                continue

            if 0 <= position < 3:
                break

            print("Please enter a position between 0 and 2.")

        return position
