# make a 3 in 1 game
# • 0 : empty
# • 1 : ocupied by player 1
# • 2 : ocupied by computer

import random


def createBoard():
    board = []
    for i in range(3):
        board.append([0, 0, 0])
    return board


def printBoard(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" ", end="")
            elif board[i][j] == 1:
                print("X", end="")
            else:
                print("O", end="")
            if j < 2:
                print("|", end="")
        print()


def checkWinner(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    return 0


def checkDraw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def checkValidMove(board, x, y):
    if x >= 0 and x < 3 and y >= 0 and y < 3 and board[x][y] == 0:
        return True
    return False


def makeMove(board, x, y, player):
    if checkValidMove(board, x, y):
        board[x][y] = player
        return True
    return False


def computerMove(board):
    for i in range(3):
        for j in range(3):
            if checkValidMove(board, i, j):
                board[i][j] = 2
                if checkWinner(board) == 2:
                    return True
                board[i][j] = 0
    for i in range(3):
        for j in range(3):
            if checkValidMove(board, i, j):
                board[i][j] = 1
                if checkWinner(board) == 1:
                    board[i][j] = 2
                    return True
                board[i][j] = 0
    while True:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if checkValidMove(board, x, y):
            board[x][y] = 2
            return True


def main():
    board = createBoard()
    winner = 0
    while winner == 0:
        printBoard(board)
        while True:
            x = int(input("Columna: "))
            y = int(input("Fila: "))
            if makeMove(board, x, y, 1):
                break
            print("Movimiento invalido")
        winner = checkWinner(board)
        if winner != 0 or checkDraw(board):
            break
        computerMove(board)
        winner = checkWinner(board)
    printBoard(board)
    if winner == 1:
        print("Has ganado!")
    elif winner == 2:
        print("Has perdido!")
    else:
        print("Dibuja!")


main()
