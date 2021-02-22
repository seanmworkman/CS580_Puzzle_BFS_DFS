# CS580_Puzzle_BFS_DFS
This program implements a Breadth-First-Search and a Depth-First-Search of the 24 puzzle problem.

To run with output in the terminal:
- Run `python3 puzzle.py BFS` for Breadth-First-Search
- Run `python3 puzzle.py DFS` for Depth-First-Search

To run with output in a txt file:
- Run `python3 puzzle.py BFS > bfs_output.txt` for Breadth-First-Search
- Run `python3 puzzle.py DFS > dfs_output.txt` for Depth-First-Search

Options:
- Add `--quiet` to any of the above commands for a quiet run, this means each state will not be printed only the end result described below

The end result will be `SUCCESS` or `FAILURE` followed by the elapsed time of the search

Each run randomizes the initial state of the puzzle

The goal state is:
`[1,   2,  3,  4,  5]`
`[6,   7,  8,  9, 10]`
`[11, 12, 13, 14, 15]`
`[16, 17, 18, 19, 20]`
`[21, 22, 23, 24,  0]`

