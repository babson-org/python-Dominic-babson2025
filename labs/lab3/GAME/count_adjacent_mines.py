"""
Function to count adjacent mines for a given cell.
"""

import globals
from get_adjacent_cells import get_adjacent_cells

def count_adjacent_mines(row, col, rows, cols):
    """
    Count the number of mines adjacent to a given cell.
    
    Args:
        row: Row index
        col: Column index
        rows: Total number of rows
        cols: Total number of columns
    
    Returns:
        int: Number of adjacent mines
    """
    count = 0
    adjacent_cells = get_adjacent_cells(row, col, rows, cols)
    
    for adj_row, adj_col in adjacent_cells:
        if globals.base_board[adj_row][adj_col] == globals.MINE:
            count += 1
    
    return count