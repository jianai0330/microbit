from random import randint
from copy import deepcopy


def getRandomMove(board, mark):

    """
    This function will be implemented by the student as part of lab 13.  It will make a random move

    :param board: 2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :param mark: The player's mark, X or O
    :return: Always returns True
    """

    print "*** NOT IMPLEMENTED YET!! ***"

    return True


def minimax(board, player1, player2, aiMove):

    """
    This function will be implemented by the student as part of lab 13.  It will create and search a game tree for an
    optimal move

    :param board:  2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :param player1: The letter, 'X' or 'O', used by player one
    :param player2: The letter, 'X' or 'O', used by player two
    :param aiMove: True if it's the maximiser's turn and false if it's the minimiser's turn
    :return: The best move (a [x,y] where x and y are coordinates on tictactoe board) and the score of the move
    """

    print "*** NOT IMPLEMENTED YET!! ***"

    return None, 0


def getAIMove(board, player1, player2):

    """
    This function uses the minimax algorithm to make optimal moves.  Students can modify the body of this function but
    not it's heading

    :param board: 2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :param player1: The letter, 'X' or 'O', used by player one
    :param player2: The letter, 'X' or 'O', used by player two
    :return: Always returns True
    """

    # Remove these two lines when you are ready to implement minimax
    print "*** NOT IMPLEMENTED YET!! ***"
    return True
    ################################################################

    moveLegal = False

    while not moveLegal:
        playerMove, score = minimax(board, player1, player2, True)
        moveLegal = makeMove(board, playerMove, player1)

    return True


def scoreGame(board, player1, player2):

    """
    This function will be implemented by the student as part of lab 13.  It checks the board for a winner.

    :param board: 2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :param player1: The letter, 'X' or 'O', used by player one
    :param player2: The letter, 'X' or 'O', used by player two
    :return: 1 if player one wins, -1 if player two wins and 0 for all other conditions
    """

    print "*** NOT IMPLEMENTED YET!! ***"

    return 0


def getFixedMove(board, player1, player2):

    """
    This function will be implemented by the student as part of lab 13 challenge task.  It will make a move based on
    a fixed strategy, i.e., set of rules.

    :param board: 2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :param player1: The letter, 'X' or 'O', used by player one
    :param player2: The letter, 'X' or 'O', used by player two
    :return: Always returns True
    """

    print "*** NOT IMPLEMENTED YET!! ***"

    return True


def getHumanMove(board, mark, player = 1):

    """
    This functions allows a user to enter his or her moves

    :param board: 2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :param mark: The player's mark, X or O
    :param player: The player's order, e.g., first or second player
    :return: True if the move is legal and not termination flag (negative value); false if termination value (<0)
    """

    playerMove = input("Player " + str(player) + ", enter a move (e.g. 1,1) : ")
    moveLegal = makeMove(board, playerMove, mark)

    while not moveLegal:
        playerMove = input("Enter move, e.g. 1,1 : ")
        moveLegal = makeMove(board, playerMove, mark)

    if playerMove[0] < 0 or playerMove[1] < 0:
        return False

    return True


def drawBoard(board):

    """
    This function displays the game on the screen.  It can only display the letters X and O.

    :param board: 2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    """

    letterX = ['  X     X  ', '   X   X   ', '    X X    ', '     X     ', '    X X    ', '   X   X   ', '  X     X  ']
    letterO = ['   OOOOO   ', '  O     O  ', '  O     O  ', '  O     O  ', '  O     O  ', '  O     O  ', '   OOOOO   ']

    tmp = []
    tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))
    for i in range(3):
        row = board[i]

        for j in range(7):
            msg = ""
            for k in range(3):
                if row[k] == 'X':
                    msg += letterX[j]
                elif row[k] == 'O':
                    msg += letterO[j]
                else:
                    msg += ' ' * 11

                if k != 2:
                    msg += '@'

            tmp.append(msg)

        if i != 2:
            tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))
            tmp.append('@' * 35)
            tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))

    tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))
    print "\n\n"
    for line in tmp:
        print line
    print "\n\n"


def makeMove(board, location, mark):

    """
    This function puts a letter (or mark) on the board if it's legal to do so.

    :param board:  2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :param location: A list, [x,y] where x and y are coordinates on tictactoe board (1 <= x <= 3 and 1 <= y <= 3)
    :param mark: The letter, 'X' or 'O'
    :return: True if x, y is within bounds and the square has not been marked already or x,y are less than 0; false
    for all other conditions
    """

    if 1 <= location[0] <= 3 and 1 <= location[1] <= 3:

        if board[location[1] - 1][location[0] - 1] != '*':
            return False

        board[location[1] - 1][location[0] - 1] = mark

        drawBoard(board)
        return True

    if location[0] < 0 or location[1] < 0:
        return True

    return False


def isGameWon(board, mark):

    """
    This function checks to see if a player, specified by mark, has won the game

    :param board:  2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :param mark: The letter, 'X' or 'O'
    :return: True if the player has won the game false if he or she has not won
    """

    for r in range(3):
        row = board[r]
        if isSameAs(mark, row[0], row[1], row[2]):
            return True

    for c in range(3):
        if isSameAs(mark, board[0][c], board[1][c], board[2][c]):
            return True

    if isSameAs(mark, board[0][0], board[1][1], board[2][2]):
        return True

    if isSameAs(mark, board[0][2], board[1][1], board[2][0]):
        return True

    return False


def isSameAs(char, a, b, c):

    """
    This function checks if all four parameters are equal

    :param char:  The letter, 'X' or 'O'
    :param a: The letter, 'X', 'O' or '*'
    :param b: The letter, 'X', 'O' or '*'
    :param c: The letter, 'X', 'O' or '*'
    :return: True if all four characters are the same otherwise false is returned
    """

    if char == a and a == b and b == c:
        return True

    return False


def getAllPossibleMoves(board):

    """
    This function returns a list containing all the possible remaining moves in a game, i.e., any position(s) on
    the board that have not been marked

    :param board:  2D List that represents the tictactoe board (empty squares are denotes with a single asterisk)
    :return: List containing x, y coordinates on the board (each coordinate is a list [x,y])
    """

    moves = []

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '*':
                moves.append([c+1,r+1])

    return moves

