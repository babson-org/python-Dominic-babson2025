def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            # Converts the input to an integer
            move = int(input(prompt))
            # Changes the range of inputted indexes from 1-9 to 0-8
            idx = move - 1
            # Checks if the inputted number is between 1 and 9
            if idx < 0 or idx > 8:
                prompt = "That isn't between 1-9. Try again (1-9): "
                 # Checks if the position is taken or not
            if board[idx] in (10, -10):
                prompt("That one's taken. Pick another: ")
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "

        board[idx + 1] = score['player']
    
    
pass
