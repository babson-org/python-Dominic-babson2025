"""
Function to get and validate user input
"""

import globals as g

def get_validated_input():
    """
    Get and validate user's cell choice
    
    Returns:
        Tuple (row, col) of valid cell coordinates
    """
    while True:
        try:
            user_input = input(f"Enter row and column (0-{g.rows-1}, 0-{g.cols-1}): ")
            parts = user_input.split()
            
            if len(parts) != 2:
                print("Please enter exactly two numbers separated by a space.")
                continue
            
            row = int(parts[0])
            col = int(parts[1])
            
            # Check if within bounds
            if row < 0 or row >= g.rows:
                print(f"Row must be between 0 and {g.rows-1}")
                continue
            
            if col < 0 or col >= g.cols:
                print(f"Column must be between 0 and {g.cols-1}")
                continue
            
            # Check if cell is already revealed
            if g.display_board[row][col] != g.HIDDEN:
                print("That cell is already revealed. Choose another cell.")
                continue
            
            return row, col
            
        except ValueError:
            print("Invalid input. Please enter two numbers.")
        except Exception as e:
            print(f"Error: {e}. Please try again.")