"""
Utility functions for Minesweeper game.
"""

def is_valid_cell(row, col, rows, cols):
    """
    Check if a cell position is within board boundaries.
    
    Args:
        row: Row index
        col: Column index
        rows: Total number of rows
        cols: Total number of columns
    
    Returns:
        bool: True if cell is valid, False otherwise
    """
    return 0 <= row < rows and 0 <= col < cols