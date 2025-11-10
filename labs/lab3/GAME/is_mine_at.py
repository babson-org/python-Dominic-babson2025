"""
Function to check if a cell contains a mine.
"""

import globals

def is_mine_at(row, col):
    """
    Check if there is a mine at the specified position.
    
    Args:
        row: Row index
        col: Column index
    
    Returns:
        bool: True if there's a mine at the position, False otherwise
    """
    return globals.base_board[row][col] == globals.MINE