"""
Function to initialize the game board.
"""

import globals
from place_random_mines import place_random_mines
from count_adjacent_mines import count_adjacent_mines

def initialize_board(rows, cols, num_mines):
    """
    Initialize the base board with mines and numbers, and create display board.
    
    Args:
        rows: Number of rows
        cols: Number of columns
        num_mines: Number of mines to place
    """
    # Set global variables
    globals.ROWS = rows
    globals.COLS = cols
    globals.NUM_MINES = num_mines
    
    # Create base board (initially all blank)
    globals.base_board = [[globals.BLANK for _ in range(cols)] for _ in range(rows)]
    
    # Place mines randomly
    place_random_mines(globals.base_board, rows, cols, num_mines)
    
    # Calculate numbers for non-mine cells
    for row in range(rows):
        for col in range(cols):
            if globals.base_board[row][col] != globals.MINE:
                adjacent_mines = count_adjacent_mines(row, col, rows, cols)
                if adjacent_mines > 0:
                    globals.base_board[row][col] = str(adjacent_mines)
                else:
                    globals.base_board[row][col] = globals.BLANK
    
    # Create display board (all hidden)
    globals.display_board = [[globals.HIDDEN for _ in range(cols)] for _ in range(rows)]