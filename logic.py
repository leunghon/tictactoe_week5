import random


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def board_with_space(board):
    for row in board:
        for block in row:
            if block == None:
                return True
    return False 

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 'X'
        elif board[0][0] == 'O':
            return 'O'
    elif board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] == 'X':
            return 'X'
        elif board[0][0] == 'O':
            return 'O'
    elif board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] == 'X':
            return 'X'
        elif board[1][0] == 'O':
            return 'O'
    elif board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] == 'X':
            return 'X'
        elif board[2][0] == 'O':
            return 'O'  
    elif board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == 'X':
            return 'X'
        elif board[2][0] == 'O':
            return 'O'
    elif board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == 'X':
            return 'X'
        elif board[0][0] == 'O':
            return 'O'
    elif board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] == 'X':
            return 'X'
        elif board[0][1] == 'O':
            return 'O'
    elif board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] == 'X':
            return 'X'
        elif board[0][2] == 'O':
            return 'O'
    else:
        return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    elif player == 'O':
        return 'X'

def make_move(board, player, x, y):
    board[x - 1][y - 1] = player
    return board

def empty_spot(board, x, y):
    if board[x - 1][y - 1] == None:
        return True
    return False

class bot:
    def __init__(self, player):
        self.player = player
    
    def move(board, player):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if empty_spot(board, x, y) is True:
            return make_move(board, player,x, y)
        return bot.move(board, player)

    def name(self):
        return self.player