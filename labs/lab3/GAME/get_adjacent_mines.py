"""
Function to get adjacent cells for a given position.
"""

from utils import is_valid_cell

def get_adjacent_cells(row, col, rows, cols):
    """
    Get all valid adjacent cells (8 neighbors: N, NE, E, SE, S, SW, W, NW).
    
    Args:
        row: Current row index
        col: Current column index
        rows: Total number of rows
        cols: Total number of columns
    
    Returns:
        list: List of tuples (row, col) for valid adjacent cells
    """
    adjacent = []
    
    # All 8 directions: N, NE, E, SE, S, SW, W, NW
    directions = [
        (-1, 0),   # N
        (-1, 1),   # NE
        (0, 1),    # E
        (1, 1),    # SE
        (1, 0),    # S
        (1, -1),   # SW
        (0, -1),   # W
        (-1, -1)   # NW
    ]
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if is_valid_cell(new_row, new_col, rows, cols):
            adjacent.append((new_row, new_col))
    
    return adjacent