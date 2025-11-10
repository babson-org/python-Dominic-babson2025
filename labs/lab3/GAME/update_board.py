"""
Function to update the display board after a move.
"""

import globals
from get_adjacent_cells import get_adjacent_cells

def update_board(row, col):
    """
    Update the display board based on the player's move.
    Uses flood-fill algorithm for blank cells.
    
    Args:
        row: Row of the selected cell
        col: Column of the selected cell
    
    Returns:
        bool: True if player hit a mine, False otherwise
    """
    # Check if it's a mine
    if globals.base_board[row][col] == globals.MINE:
        # Reveal all mines
        for r in range(globals.ROWS):
            for c in range(globals.COLS):
                if globals.base_board[r][c] == globals.MINE:
                    globals.display_board[r][c] = globals.MINE
        return True  # Game over
    
    # If it's a number, just reveal it
    if globals.base_board[row][col] != globals.BLANK:
        globals.display_board[row][col] = globals.base_board[row][col]
        return False
    
    # If it's blank, do flood-fill using a stack
    stack = [(row, col)]
    visited = set()
    
    while stack:
        curr_row, curr_col = stack.pop()
        
        # Skip if already visited
        if (curr_row, curr_col) in visited:
            continue
        
        visited.add((curr_row, curr_col))
        
        # Reveal the current cell
        globals.display_board[curr_row][curr_col] = globals.base_board[curr_row][curr_col]
        
        # If current cell is blank, add all adjacent cells to stack
        if globals.base_board[curr_row][curr_col] == globals.BLANK:
            adjacent = get_adjacent_cells(curr_row, curr_col, globals.ROWS, globals.COLS)
            for adj_row, adj_col in adjacent:
                # Only add if not already revealed and not visited
                if (adj_row, adj_col) not in visited:
                    if globals.display_board[adj_row][adj_col] == globals.HIDDEN:
                        # Always add blank cells
                        if globals.base_board[adj_row][adj_col] == globals.BLANK:
                            stack.append((adj_row, adj_col))
                        # Also reveal numbers at the border
                        elif globals.base_board[adj_row][adj_col] != globals.MINE:
                            globals.display_board[adj_row][adj_col] = globals.base_board[adj_row][adj_col]
    
    return False  # Game continues