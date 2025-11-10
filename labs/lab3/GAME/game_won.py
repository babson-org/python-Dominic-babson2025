"""
Function to check if the game has been won.
"""

import globals

def game_won():
    """
    Check if all non-mine cells have been revealed.
    
    Returns:
        bool: True if game is won, False otherwise
    """
    for row in range(globals.ROWS):
        for col in range(globals.COLS):
            # If there's a hidden cell that's not a mine, game is not won
            if globals.display_board[row][col] == globals.HIDDEN:
                if globals.base_board[row][col] != globals.MINE:
                    return False
    
    return True