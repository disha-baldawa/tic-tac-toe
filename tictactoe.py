"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
SIZE = 3

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # count the occurences of x and o in the board to check whose chance it is
    x_count = sum(i.count('X') for i in board)
    o_count = sum(i.count('O') for i in board)
    if x_count == o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    actions = [(i,j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == EMPTY]
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action # tuple
    board_copy = copy.deepcopy(board)
    # to not modify the original board
    if board[i][j] == EMPTY:
        # add the current player's symbol at location (i,j) in board_copy
        board_copy[i][j] = player(board)
        return board_copy
    else:
        raise Exception("Move not possible.")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkWinner(X, board):
        return X
    elif checkWinner(O, board):
        return O
    else:
        return None
    

def checkWinner(player, board):
    # to count for horizontal wins
    for row in range(SIZE):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # to count fot vertical wins
    for col in range(SIZE):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # to count for right diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    # to count for left diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
   

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in range(SIZE):
        for col in range(SIZE):
            # if there is a single space empty, the game isn't over
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        # maximize
        return 1
    elif winner(board) == O:
        # minimize
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # for X
    def max_value(state):
        if terminal(state):
            return utility(state), None
        v = -float("inf")
        # going through each possible action one can play
        for action in actions(state):
            # calling min_value for O's turn
            new_v = min_value(result(state, action))[0]
            if new_v > v:
                v = new_v
                max_action = action
        return v, max_action

    # for O
    def min_value(state):
        if terminal(state):
            return utility(state), None
        v = float("inf")
        for action in actions(state):
            new_v = max_value(result(state, action))[0]
            if new_v < v:
                v = new_v
                min_action = action
        return v, min_action 

    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
