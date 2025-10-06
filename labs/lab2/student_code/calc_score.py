def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """
     
    def line_sum(a, b, c):
        '''
            line_sum takes 3 numbers and if the sum is either 30
            or -30 returns that sum otherwise do not return
        '''         
         
        # Sums the values at board[a], board[b], board[c] 
        total = board[a] + board[b] + board[c]
        # Returns 30 if X wins, -30 if O wins otherwise do not return
        if total == 30:
            return 30
        elif total == -30:
            return -30
     
    # Lists each way that a player can win
    wins_list = [(0,1,2), (3,4,5), (6,7,8), (2,4,6), (0,4,8), (2,5,8), (1,4,7)]
    # Uses line_sum to find the values in each section, returns 30 or -30 for a win
    for a, b, c in wins_list:
        sum1 = line_sum(a, b, c)
        if sum1 == 30 or -30:
            return 0
    pass

