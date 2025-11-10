"""
Function to get and validate user input.
"""

import globals

def get_validated_input(prompt, min_val, max_val):
    """
    Get validated integer input from user within a specified range.
    
    Args:
        prompt: String to display to user
        min_val: Minimum acceptable value
        max_val: Maximum acceptable value
    
    Returns:
        int: Valid integer within range
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_move():
    """
    Get a valid move (row, col) from the player.
    
    Returns:
        tuple: (row, col) representing the player's move
    """
    print("\nEnter your move:")
    row = get_validated_input(f"Row (0-{globals.ROWS-1}): ", 0, globals.ROWS - 1)
    col = get_validated_input(f"Column (0-{globals.COLS-1}): ", 0, globals.COLS - 1)
    
    # Check if cell is already revealed
    if globals.display_board[row][col] != globals.HIDDEN:
        print("That cell is already revealed. Choose another.")
        return get_move()
    
    return row, col