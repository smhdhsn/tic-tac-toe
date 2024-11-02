def read_player_marker(msg: str) -> str:
    """
    Reads player's marker from input.

    Raises:
        ValueError: If user's input is not 'X' or 'O'.

    Returns:
        str: User's marker.
    """
    s = input(msg).strip().upper()

    if s not in {"X", "O"}:
        raise ValueError("Please enter either 'X' or 'O'.")

    return s
