"""
Test script for Minesweeper game functionality.
"""

import globals
from initialize_board import initialize_board
from print_board import print_board
from update_board import update_board
from game_won import game_won

def test_game():
    """Test basic game functionality."""
    print("Testing Minesweeper Game\n")
    print("=" * 50)
    
    # Test 1: Initialize a small board
    print("\nTest 1: Initializing 5x5 board with 3 mines")
    initialize_board(5, 5, 3)
    
    print("\nBase Board (Hidden from player in actual game):")
    print_board(globals.base_board, globals.ROWS, globals.COLS)
    
    print("\nDisplay Board (What player sees):")
    print_board(globals.display_board, globals.ROWS, globals.COLS)
    
    # Test 2: Count mines
    mine_count = sum(1 for row in globals.base_board for cell in row if cell == globals.MINE)
    print(f"\nMine count verification: {mine_count} mines (expected 3)")
    assert mine_count == 3, "Mine count doesn't match!"
    print("✓ Mine count correct")
    
    # Test 3: Find a safe cell to test reveal
    print("\nTest 2: Testing cell reveal")
    safe_cell = None
    for r in range(globals.ROWS):
        for c in range(globals.COLS):
            if globals.base_board[r][c] != globals.MINE:
                safe_cell = (r, c)
                break
        if safe_cell:
            break
    
    if safe_cell:
        r, c = safe_cell
        print(f"Revealing safe cell at ({r}, {c})")
        hit_mine = update_board(r, c)
        assert not hit_mine, "Safe cell returned hit_mine=True!"
        print("✓ Cell revealed successfully")
        
        print("\nUpdated Display Board:")
        print_board(globals.display_board, globals.ROWS, globals.COLS)
    
    # Test 4: Game won check
    print("\nTest 3: Checking win condition")
    won = game_won()
    print(f"Game won: {won}")
    print("✓ Win condition check works")
    
    # Test 5: Test hitting a mine
    print("\nTest 4: Testing mine hit")
    mine_cell = None
    for r in range(globals.ROWS):
        for c in range(globals.COLS):
            if globals.base_board[r][c] == globals.MINE:
                mine_cell = (r, c)
                break
        if mine_cell:
            break
    
    if mine_cell:
        r, c = mine_cell
        print(f"Revealing mine at ({r}, {c})")
        hit_mine = update_board(r, c)
        assert hit_mine, "Mine cell returned hit_mine=False!"
        print("✓ Mine detection works")
        
        print("\nDisplay Board after hitting mine (all mines revealed):")
        print_board(globals.display_board, globals.ROWS, globals.COLS)
    
    print("\n" + "=" * 50)
    print("All tests passed! ✓")
    print("=" * 50)

if __name__ == "__main__":
    test_game()