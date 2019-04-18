from Game import *

# TicTacToe
# Author: Jeffery Raphael
# Jan. 2019

def main():

    board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    moveCount = 0
    isPlaying = True
    firstPlayer = True

    player1 = 'X'
    player2 = 'O'
    machine = 'HUMAN'
    drawBoard(board)

    while isPlaying:

        if firstPlayer:
            mark = player1
            playerMove = getHumanMove(board, player1)
            firstPlayer = False
        else:
            firstPlayer = True
            mark = player2

            if machine == 'RANDOM':
                playerMove = getRandomMove(board, player2)
            elif machine == 'MINIMAX':
                playerMove = getAIMove(board, player2, player1)
            elif machine == 'FIXED':
                playerMove = getFixedMove(board, player2, player1)
            else:
                playerMove = getHumanMove(board, player2, 2)

        if playerMove:

            moveCount += 1
            won = isGameWon(board, mark)

            if won:
                isPlaying = False

                if firstPlayer:
                    print "\n\n Player 2 WON!!!\n\n"
                else:
                    print "\n\n Player 1 WON!!!\n\n"
        else:
            isPlaying = False

        if moveCount == 9 and isPlaying:

            isPlaying = False
            print "\n\nIT'S A DRAW!\n\n"


main()
