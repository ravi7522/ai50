"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    #initlizing the both x and o counter to zero
    countx = 0
    counto = 0
    
    #looping over to count the no of occurancces of x and o in the board
    for i in range(3):                  
        for j in range(3):
            #increamenting the counter of x and o based on the board
            if board[i][j] == O:
                counto += 1
            elif board[i][j] == X:
                countx +=1
    
    #after counting returning the player whose turn is
    #both are zero means there is no element in board so by default its x's turn
    if countx == counto:
        return X
    #value if x is greater than o so its o's turn
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #creating an empty set to contain all possible actions on the board
    possible_moves = set()
    
    #looping over board to get the possible actions
    for i in range(3):
        for j in range(3):
            #finding the empty and adding it to the possible_moves set
            if board[i][j] == EMPTY:
                #appending data to possible_move set
                possible_moves.add((i,j))
    
#    returning the possible outcomes available for the next player
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #getting the value if i and j from the action
    (i, j) = action
    
    #checking for exception on the board for i,j position
    if i < 3 and j < 3 and board[i][j] is EMPTY:
        player_sign = player(board)         #getting sign of player
        new_board = copy.deepcopy(board)    #creating a copy of board
        new_board[i][j] = player_sign       #doing the action
        #returning the new board
        return new_board
    else:
        #implementing the exception error message
        raise Exception("Invalid Action !!!")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #checking the values in each row and selecting the winner based on rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return "X"
        if board[i][0] == board[i][1] == board[i][2] == "O":
            return "O"
    
    #checking the values in each column and selecting the winner based on columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == "X":
            return "X"
        if board[0][j] == board[1][j] == board[2][j] == "O":
            return "O"
        
    #checking the digonally on both side and evaluting the winner based on that
    if board[0][0] == board[1][1] == board[2][2] == "X":
        return "X"
    if board[0][0] == board[1][1] == board[2][2] == "O":
        return "O"
    
    if board[2][0] == board[1][1] == board[0][2] == "X":
        return "X"
    if board[2][0] == board[1][1] == board[0][2] == "O":
        return "O"

    #if none of this is true then returning none as output
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if there is any winner then returning true
    if winner(board) != None:
        return True
    #checking whether all the spaces in the board is filled or not ?
    if any(None in row for row in board):
        return False
    else:
        return True
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #getting the winner
    winner_player = winner(board)
    
    #returning the value according to the winner
    if winner_player == "X":
        return 1
    elif winner_player == "O":
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board):
        best_val = -1
        best_move = (-1, -1)
        c = sum(row.count(EMPTY) for row in board)
        if c == 9:
            return best_move
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val == 1:
                best_move = action
                break
            if move_val > best_val:
                best_move = action
        return best_move
    
    if player(board) == "O":
        best_val = 1
        best_move = (-1, -1)
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val == -1:
                best_move = action
                break
            if move_val < best_val:
                best_move = action
        return best_move
    
def min_value(board):
    """
    
    """
    if terminal(board):
        return utility(board)
    val = 1
    for action in actions(board):
        val = min(val, max_value(result(board, action)))
        if val == -1:
            break
    return val

def max_value(board):
    """
    
    """
    if terminal(board):
        return utility(board)
    val = 1
    for action in actions(board):
        val = max(val, min_value(result(board, action)))
        if val == 1:
            break
    return val