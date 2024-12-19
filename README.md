# Tic-Tac-Toe Game – Minimax Algorithm

This project is a modular, object-oriented implementation of Tic-Tac-Toe that includes a state-space search, AI decision-making (via Minimax), and a clear, extensible code structure. It provides:

- **State Space Generation**: Dynamically create a searchable graph of all possible game states.
- **Minimax AI**: Compute optimal moves for the AI agent using a classic adversarial search algorithm.
- **Rule Enforcement & Utilities**: Ensure fair play with robust rules, easy board manipulation, and result announcements.
- **Modular Design**: Clean separation of concerns makes the code easy to navigate, maintain, and extend.

Ideal for those who want to explore how turn-based games can be modeled as state spaces and solved (or played optimally) using AI search strategies.

## Project Structure

```sh
.
├── Makefile                     # Build and execution tasks (run, state_space generation, lint)
├── app/                         # High-level application logic
│   ├── __init__.py
│   ├── state_space/
│   │   └── main.py              # Generates or manages the full state space
│   └── tic_tac_toe/
│       ├── __init__.py
│       └── main.py              # Entry point for running the Tic-Tac-Toe application
├── dto/
│   ├── __init__.py
│   └── position.py              # Position dataclass (row/column) for moves
├── game/
│   ├── __init__.py
│   ├── algorithm.py             # Orchestrates the game loop, integrates players, prints board, applies rules
│   └── rules.py                 # Defines game logic: turn determination, winner checks, board fullness, utility
├── helpers/
│   ├── __init__.py
│   ├── announce.py              # Announces game results (win/draw)
│   └── mark.py                  # Gets user input to decide player marks (X/O)
├── models/
│   ├── __init__.py
│   ├── agent.py                 # AI player implementation: loads state space, uses minimax for moves
│   ├── board.py                 # Board class: 3x3 grid, mark placement, hashing utility
│   ├── human.py                 # Human player: prompts user for next move
│   ├── mark.py                  # Mark enum (X, O, EMPTY)
│   ├── player.py                # Abstract player class (human or AI must implement get_next_move)
│   └── state.py                 # State class: represents nodes in the game tree, tracks child states
├── requirements.txt             # Python dependencies
├── search/
│   ├── __init__.py
│   ├── frontier.py              # Frontier (queue) for exploring states in state space searches
│   ├── minimax.py               # Minimax implementation (max_value/min_value functions)
│   └── state_space.py           # StateSpace class: builds and stores the entire state graph recursively
└── views/
    ├── __init__.py
    └── board.py                 # Functions for rendering the board in the console
