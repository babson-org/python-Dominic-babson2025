"""
Main Minesweeper game implementation.
"""

import globals
from initialize_board import initialize_board
from print_board import print_board
from get_validated_input import get_validated_input, get_move
from update_board import update_board
from game_won import game_won

def play_minesweeper():
    """
    Main function to play Minesweeper game.
    """
    print("=" * 40)
    print("Welcome to Minesweeper!")
    print("=" * 40)
    
    # Get board dimensions
    print("\nBoard Setup:")
    rows = get_validated_input("Enter number of rows (5-20): ", 5, 20)
    cols = get_validated_input("Enter number of columns (5-20): ", 5, 20)
    
    # Get number of mines
    max_mines = (rows * cols) // 3  # Max 1/3 of board can be mines
    num_mines = get_validated_input(f"Enter number of mines (1-{max_mines}): ", 1, max_mines)
    
    # Initialize the game board
    print("\nInitializing game...")
    initialize_board(rows, cols, num_mines)
    
    print("\nGame Instructions:")
    print(f"- The board is {rows}x{cols} with {num_mines} mines")
    print(f"- Symbol {globals.HIDDEN} = hidden cell")
    print(f"- Symbol {globals.MINE} = mine")
    print("- Numbers show how many mines are adjacent")
    print("- Blank cells have no adjacent mines")
    print("\nLet's play!\n")
    
    # Game loop
    game_over = False
    
    while not game_over:
        # Display current board
        print_board(globals.display_board, globals.ROWS, globals.COLS)
        
        # Get player's move
        row, col = get_move()
        
        # Update board based on move
        hit_mine = update_board(row, col)
        
        if hit_mine:
            print("\n" + "=" * 40)
            print_board(globals.display_board, globals.ROWS, globals.COLS)
            print("=" * 40)
            print("💥 BOOM! You hit a mine!")
            print("Game Over - You Lose!")
            print("=" * 40)
            game_over = True
        elif game_won():
            print("\n" + "=" * 40)
            print_board(globals.display_board, globals.ROWS, globals.COLS)
            print("=" * 40)
            print("🎉 Congratulations! You cleared all the mines!")
            print("You Win!")
            print("=" * 40)
            game_over = True
        else:
            print()  # Blank line for readability


if __name__ == "__main__":
    play_minesweeper()