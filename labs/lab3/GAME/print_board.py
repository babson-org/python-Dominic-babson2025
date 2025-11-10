"""
Function to print the Minesweeper board.
"""

def print_board(board, rows, cols):
    """
    Print the game board with row and column headers.
    
    Args:
        board: 2D list representing the board
        rows: Number of rows
        cols: Number of columns
    """
    # Print column headers
    print("  ", end="")
    for col in range(cols):
        print(f"{col} ", end="")
    print()
    
    # Print each row with row header
    for row in range(rows):
        print(f"{row} ", end="")
        for col in range(cols):
            cell_value = board[row][col]
            # Display blank cells as spaces, everything else as-is
            if cell_value == ' ' or cell_value == '':
                print("  ", end="")
            else:
                print(f"{cell_value} ", end="")
        print()