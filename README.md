# SudokuSolverPython

The program starts by entering a cell in the Sudoku grid and compile a list of any numbers that can be legally placed in that grid. It checks the rows, columns and the 3x3 sub-grids, and if the list of legal numbers is larger than 0 it plots in the first number on that list in said cell, and proceeds to go to the next empty cell. This process is repeated until the entire board is either solved, or there is no more legal numbers to find in the cell. If the latter is true, we resort to Backtracking. This means reverting the state of the Sudoku board, so that we can attempt a different number in our list of legal numbers. The list is actually a set, so the order of the numbers will always be random, as well as it allows us to use set operators when checking the list against what's already on the board.

https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#backtracking

