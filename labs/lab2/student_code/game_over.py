
from calc_score import calc_score


def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """

    # Chekcs if all of the spots on the board are filled
    if all(abs(board) == 10 ):
        return True
    # Uses calc_score to check if someone has won, returns true if game is over, false if not
    score = calc_score(board)
    if score == 30 or score == -30:
        return True
    else:
        return False
