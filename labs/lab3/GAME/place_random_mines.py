"""
Function to place mines randomly on the board.
"""

import random
import globals

def place_random_mines(board, rows, cols, num_mines):
    """
    Randomly place mines on the board.
    
    Args:
        board: 2D list representing the board
        rows: Number of rows
        cols: Number of columns
        num_mines: Number of mines to place
    """
    mines_placed = 0
    
    while mines_placed < num_mines:
        # Generate random position
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        # Only place mine if cell doesn't already have one
        if board[row][col] != globals.MINE:
            board[row][col] = globals.MINE
            mines_placed += 1