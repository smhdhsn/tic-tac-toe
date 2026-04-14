"""
This package defines the player for the Tic-Tac-Toe game.
"""

from .mark import Mark

class Player:
    """
    Player is the class for a player in Tic-Tac-Toe game.
    """

    def __init__(self, mark: Mark) -> None:
        """
        Initializes a player with given mark.

        Args:
            mark (Mark): The mark for this player.

        Raises:
            ValueError: If the given mark is not an instance of the Mark.
        """

        if not isinstance(mark, Mark):
            raise ValueError("Given mark must be an instance of Mark class.")

        self.mark: Mark = mark

    def get_mark(self) -> Mark:
        """
        Retrieves the mark of this player.

        Returns:
            Mark: The mark of this player.
        """

        return self.mark
