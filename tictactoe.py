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
    x_count = sum(i.count('X') for i in board)
    o_count = sum(i.count('O') for i in board)
    # for i in range(SIZE):
    #     for j in range(SIZE):
    #         if board[i][j] == X:
    #             x_count += 1
    #         if board[i][j] == O:
    #             o_count += 1
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
    # for i in range(SIZE):
    #     for j in range(SIZE):
    #         if board[i][j] == EMPTY:
    #             actions.add((i,j))
    # print(actions)
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action #tuple
    # move = 
    board_copy = copy.deepcopy(board)
    # to not modify the original board
    if board[i][j] == EMPTY:
        board_copy[i][j] = player(board)
        return board_copy
    else:
        raise Exception("Move not possible.")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkWinner(X, board).count(True) == 1:
        return X
    elif checkWinner(O, board).count(True) == 1:
        return O
    else:
        return None
    

def checkWinner(player, board):
    lst = []
    for row in range(SIZE):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            lst.append(True)
            break
        # else:
        #     lst.append(False)
    for col in range(SIZE):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            lst.append(True)
            break
        # else:
        #     lst.append(False)
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        lst.append(True)
    # else:
    #         lst.append(False)
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        lst.append(True)
    # else:
    #         lst.append(False)
    return lst
   

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in SIZE:
        for col in SIZE:
            if board[row][col] == EMPTY:
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
            return utility(state)
        v = -float("inf")
        for action in actions(state):
            new_v = min_value(result(state, action))[0]
            if new_v > v:
                v = new_v
                max_action = action
        return v, max_action

    def min_value(state):
        if terminal(state):
            return utility(state)
        v = float("inf")
        for action in actions(state):
            new_v = max_value(result(state, action))[0]
            if new_v < v:
                v = new_v
                min_action = action
        return v, min_action 

    if player(board) == X:
        return max_value(board)
    else:
        return min_value(board)
