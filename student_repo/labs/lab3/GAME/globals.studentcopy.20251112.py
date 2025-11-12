MINE = "💣"
HIDDEN = "⬧"
EMPTY = " "
def get_board_dimensions(ROWS, COLS):
    ROWS = int(input("Enter number of rows: "))
    COLS = int(input("Enter number of columns: "))
    NUM_MINES = int(input("Enter number of mines: "))
    while True:
        if ROWS <= 0 or COLS <= 0:
            raise ValueError("Rows and columns must be positive integers.")
        elif NUM_MINES >= ROWS * COLS:
            raise ValueError("Number of mines must be less than total cells.")
        elif NUM_MINES < 0:
            raise ValueError("Number of mines cannot be negative.")
        break
        if num_mines >= rows * cols:
            raise ValueError("Number of mines must be less than total cells.")
        break
    print("Input values are valid.")

