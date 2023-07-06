

# Eight Puzzle Solver

This project is an implementation of various search algorithms to solve the eight puzzle, which is a smaller version of the well-known sliding block puzzle known as the "fifteen puzzle". The project is structured in an object-oriented way, providing classes for the state-space search, state representation, board configuration, and utility classes for timing operations.

## File Descriptions

1. `searcher.py` - This file contains the logic for state-space search algorithms, including uninformed random search, breadth-first search (BFS), depth-first search (DFS), greedy search and A* search.

2. `state.py` - This file defines a State class for representing states in the search tree of the Eight Puzzle. Each state includes a board configuration, the move that led to it, and a link to its predecessor.

3. `board.py` - This file provides the Board class for representing configurations of the Eight Puzzle.

4. `timer.py` - This file defines a Timer class that is used to measure the time elapsed during operations, mainly for performance testing.

## Installation

The project is written in Python. Make sure you have a Python environment set up and clone the project using git:

```
git clone https://github.com/username/Eight-Puzzle-Solver.git
cd Eight-Puzzle-Solver
```

## Usage

After you've cloned the project, you can run the program with your desired puzzle configuration:

```python
#Using an interactive window simply type:

eight_puzzle(board, algorithm, heuristic)

#board: A string that tells the program the initial state of a board. Here is an example "123506478", it's important to choose a string that can be solved. Not all initial states have a soultion.

#algorithm: A string that tells the function which algorithm to use for finding a solution

#heuristic: A heuristic function used by some of the algorithms
```

This code will print the sequence of moves from the initial state to the solution. Note that the actual sequence will depend on the search algorithm used. For example, BFS might give a different sequence than A* search.

## Contributing

If you're interested in contributing, please follow the standard Fork & Pull Request workflow.

## Authors

- **Jose Ramirez** - *Initial work* - [nowaymyname27](https://github.com/nowaymyname27)

---

Remember to replace "Your Name" and "YourUsername" with your actual name and GitHub username.
