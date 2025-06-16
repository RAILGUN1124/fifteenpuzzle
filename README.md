# Fifteen Puzzle Solver

This project implements a Fifteen Puzzle game with multiple solving strategies, including human interaction and automated solvers using A* and IDA* algorithms. The game is built using Python and `pygame` for visualization.

## Project Structure


### Key Components

1. **`main.py`**  
   The entry point of the application. It allows the user to choose between playing the game manually or solving it using A* or IDA* algorithms. It provides the following command-line arguments:
   - `--human`: Play the game manually.
   - `--a-star`: Solve the puzzle using the A* algorithm.
   - `--ida-star`: Solve the puzzle using the IDA* algorithm.

2. **`data/classes/FifteenPuzzle.py`**  
   Implements the game board logic, including:
   - Generating and managing the puzzle tiles.
   - Handling moves and checking if the puzzle is solved.
   - Drawing the puzzle on the screen using `pygame`.

3. **`data/classes/Square.py`**  
   Represents individual tiles (squares) on the puzzle board. Handles:
   - Tile properties like position, size, and value.
   - Drawing the tile on the screen.

4. **`data/classes/HumanPlayer.py`**  
   Allows a human player to interact with the puzzle. Handles:
   - Mouse input to select and move tiles.
   - Integration with the `FifteenPuzzle` class for move validation.

5. **`data/classes/AStarSolver.py`**  
   Implements the A* algorithm for solving the puzzle. Features:
   - Heuristics like Manhattan distance, linear conflict, and walking distance.
   - Efficient pathfinding using a priority queue (`heapq`).

6. **`data/classes/IDAStarSolver.py`**  
   Implements the IDA* algorithm for solving the puzzle. Features:
   - Recursive depth-first search with iterative deepening.
   - Heuristics similar to A* for estimating the cost.

7. **`data/classes/PuzzleInstance.py`**  
   Manages the game instance. Handles:
   - Initializing the puzzle with a given configuration.
   - Running the game loop for human players.
   - Executing and timing the solvers (A* and IDA*).

### How it works 

Human Player
- The game initializes a FifteenPuzzle board with a given configuration.
- The player interacts with the board using mouse clicks to move tiles.
- The game checks if the puzzle is solved after each move.

A* Solver
- The A* algorithm uses a priority queue to explore states with the lowest estimated cost (f = g + h).
- Heuristics like Manhattan distance and linear conflict guide the search.
- The solution path is reconstructed once the goal state is reached.

IDA* Solver
- The IDA* algorithm performs iterative deepening depth-first search.
- It uses the same heuristics as A* to prune the search space.
- The algorithm terminates when the goal state is found or the bound is exceeded.

### Notes

- The game uses **pygame** for visualization, so ensure you have a graphical environment to run it.
- The solvers are designed to handle the 15-puzzle efficiently, but performance may vary for complex configurations.
  
