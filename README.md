# Tic-Tac-Toe AI (Minimax)

A command-line Tic-Tac-Toe game in Python featuring an AI opponent powered by the **Minimax algorithm**. The AI is designed to play optimally by exploring the full game state space and choosing the best possible move at every turn.

---

## 🚀 Features

* Human vs AI gameplay
* AI uses **Minimax (full game tree)**
* Precomputed **state space** for faster decisions
* Clean modular architecture (models, search, game logic)
* Input validation and error handling

---

## 🧠 How It Works

The AI:

1. Builds (or loads) a **state-space tree** of all possible Tic-Tac-Toe boards.
2. Uses **Minimax**:

   * `X` = maximizing player
   * `O` = minimizing player
3. Evaluates terminal states:

   * `+1` → X wins
   * `-1` → O wins
   * `0` → Draw
4. Chooses the move that guarantees the best outcome.

---

## 📁 Project Structure

```txt
app/
  tic_tac_toe/main.py        # Run the game
  state_space/main.py        # Generate state space

models/
  board.py                   # Board representation
  state.py                   # Game state (node)
  player.py                  # Abstract player
  human.py                   # Human player
  agent.py                   # AI player
  mark.py                    # Enum (X, O, EMPTY)

game/
  algorithm.py               # Game loop
  rules.py                   # Game rules + utility

search/
  state_space.py             # Builds game tree
  minimax.py                 # Minimax functions
  frontier.py                # Graph traversal helper

helpers/
  announce.py                # Prints result
  mark.py                    # User input

dto/
  position.py                # Board position class

views/
  board.py                   # CLI rendering
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Install dependencies

```bash
pip install beartype
```

---

## ▶️ How to Run

### Step 1: Generate state space (IMPORTANT)

```bash
python app/state_space/main.py
```

This creates:

```txt
export/state_space.pkl
```

---

### Step 2: Run the game

```bash
python app/tic_tac_toe/main.py
```

---

## 🎮 How to Play

1. Choose your mark:

```txt
Choose your mark (X or O):
```

2. Enter moves as row and column:

```txt
Row:    0
Column: 2
```

Board indices:

```txt
     0   1   2
 0   .   .   .
 1   .   .   .
 2   .   .   .
```

---

## ⚠️ Important Notes

* Always regenerate `state_space.pkl` after code changes:

```bash
rm export/state_space.pkl
python app/state_space/main.py
```

* The game assumes:

  * `X` always starts
  * AI plays optimally (cannot be beaten)

---


## 💡 Future Improvements

* Add **alpha-beta pruning**
* Add **GUI (Tkinter / Pygame / Web)**
* Add **difficulty levels**
* Add **unit tests**
* Optimize state-space storage
