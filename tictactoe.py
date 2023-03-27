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
    x_count = 0
    o_count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == X:
                x_count += 1
            if board[i][j] == O:
                o_count += 1
    if x_count == o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    move = player(board)
    board_copy = copy.deepcopy(board)
    if board[i][j] == EMPTY:
        board_copy[i][j] = move
        return board_copy
    else:
        raise Exception("Move not possible.")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    center = board[1][1]
    if center == board[0][0] and center == board[2][2]:
        return center
    elif center == board[0][2] and center == board[2][0]:
        return center
    else:
        for i in range(SIZE):
            center = board[i][1]
            if center == board[i][0] and center == board[i][2] and center != EMPTY:
                return center
        for i in range(SIZE):
            center = board[1][i]
            if center == board[0][i] and center == board[2][i] and center != EMPTY:
                return center
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(SIZE):
            for j in range(SIZE):
                if board[i][j] == EMPTY:
                    return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(state):
        if terminal(state):
            return utility(state), None
        v = -float("inf")
        for action in actions(state):
            new_v = min_value(result(state, action))[0]
            if new_v > v:
                v = new_v
                max_action = action
        return v, max_action

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
