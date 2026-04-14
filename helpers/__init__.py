"""
This module contains helper functions for the game.
"""

from .mark import decide_marks
from .announce import announce_result

# Expose methods at the package level.
__all__ = ["decide_marks", "announce_result"]
