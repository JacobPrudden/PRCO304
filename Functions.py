'''
Created on 18 Feb 2018

@author: Jacob
'''
import numpy as np

#initialises the board
def BoardInit():
    board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    return board

def BoardtoColour(board):
    boardCopy=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    a = 0
    while a<=7:
        b = 0
        while b<=7:
            if(board[a][b] == 0):
                boardCopy[a][b] = "green"
            elif(board[a][b] == 1):
                boardCopy[a][b] = "white"
            elif(board[a][b] == 2):
                boardCopy[a][b] = "black"
            b+=1
        a+=1
    return boardCopy
#returns a copy of the board state which is not a pointer to the same data
def BoardCopy(board):
    boardCopy=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    a = 0
    while a<=7:
        b = 0
        while b<=7:
            boardCopy[a][b] = board[a][b]
            b+=1
        a+=1
    return boardCopy

# Converts the python list used to represent the board into a numPy array that can be used in tensorflow
def boardToNN(board,player):
    nnBoard = np.zeros((64,1),dtype=np.int32)
    
    i = 0
    while i<=7:
        j = 0
        while j<=7:
            val = board[i][j]
            if(val == 0):
                nnBoard[i*8+j][0] = 0
            elif(val == 1):
                nnBoard[i*8+j][0] = 1
            elif(val == 2):
                nnBoard[i*8+j][0] = -1
            j+=1
        i+=1
    return nnBoard

#updates the board when a player makes a move
def MakeMove(board,y,x,player):
    impact = 0
    if(x>7 or y>7 or x<0 or y<0):#if the tile is outside of the board
        return board
    elif(board[x][y]!=0):#if there is already a piece on that tile
        return board
    xMod = -1
    end = 0
    while xMod<=1:#try moving left, no direction and right on the board
        yMod = -1
        while yMod<=1:# try moving down, no direction and up on the board
            xTemp = x
            yTemp = y
            end = 0
            while xTemp>=0 and yTemp>=0 and xTemp<8 and yTemp<8 and end == 0:# while it is within the board
                xTemp = xTemp + xMod
                yTemp = yTemp + yMod
                if(xTemp>7 or yTemp>7 or xTemp<0 or yTemp<0):# if the edges of the board are reached
                    end = 1
                elif(board[xTemp][yTemp]==0):# if a blank tile is hit
                    end = 1
                elif(board[xTemp][yTemp]==player):# if you reach a tile belonging to the player
                    while yTemp != y or xTemp != x:# until you reah the tile you placed a piece on
                        if(board[xTemp-xMod][yTemp-yMod]!= player and board[xTemp-xMod][yTemp-yMod]!= 0):
                            impact = 1
                            board[xTemp-xMod][yTemp-yMod] = player# update the piece
                        xTemp = xTemp-xMod
                        yTemp = yTemp-yMod
                    end = 1
            
            yMod = yMod + 1
        xMod = xMod + 1
    if(impact == 1):
        board[x][y] = player
    return board

#See if a move affects the board at all
def TryMove(board,y,x,player):
    #print(player)
    impact = 0
    if(x>7 or y>7 or x<0 or y<0):#if the tile is outside of the board
        return impact
    elif(board[x][y]!=0):#if there is already a piece on that tile
        return impact
    xMod = -1
    end = 0
    while xMod<=1:#try moving left, no direction and right on the board
        yMod = -1
        while yMod<=1:# try moving down, no direction and up on the board
            xTemp = x
            yTemp = y
            end = 0
            while xTemp>=0 and yTemp>=0 and xTemp<8 and yTemp<8 and end == 0:# while it is within the board
                xTemp = xTemp + xMod
                yTemp = yTemp + yMod
                if(xTemp>7 or yTemp>7 or xTemp<0 or yTemp<0):# if the edges of the board are reached
                    end = 1
                elif(board[xTemp][yTemp]==0):# if a blank tile is hit
                    end = 1
                elif(board[xTemp][yTemp]==player):# if you reach a tile belonging to the player
                    while yTemp != y or xTemp != x:
                        if(board[xTemp-xMod][yTemp-yMod]!= player and board[xTemp-xMod][yTemp-yMod]!= 0):
                            impact = 1
                        xTemp = xTemp-xMod
                        yTemp = yTemp-yMod
                    end = 1
            
            yMod = yMod + 1
        xMod = xMod + 1
    return impact

# check if the game is over
def GameOver(board):
    gameOver = 1
    player = 1
    while player<=2:
        for x in range (0,8):
            for y in range (0,8):
                impact = TryMove(board,y,x,player)
                if(impact == 1):
                    gameOver = 0
                    return gameOver
        player+=1
    #print(board)
    return gameOver

# returns the number of player 1's pieces - the number of player 2's pieces
def BlackWhiteCount(board):
    count = 0
    for i in range (0,8):
        for j in range (0,8):
            if (board[i][j] == 1):
                count+=1
            elif (board[i][j] ==2):
                count-=1
    return count

# returns the difference between the number of players 1's pieces and player 2's pieces
def BlackWhiteDiff(board):
    count = 0
    for i in range (0,8):
        for j in range (0,8):
            if (board[i][j] == 1):
                count+=1
            elif (board[i][j] == 2):
                count-=1
    return abs(count)

# return an array with all of the legal moves
def MovesAvailable(board,player):
    movesAvailable = []
    for x in range (0,8):
            for y in range (0,8):
                impact =TryMove(board,x,y,player)
                if(impact == 1):
                    movesAvailable.append([x,y])
    return movesAvailable

# returns the player who should play next
def nextPlayer(board,player):
    if(player == 1):
        player = 2
    else:
        player = 1
    movesAvailable = MovesAvailable(board,player)
    if(movesAvailable):
        return player
    else:
        if(player == 1):
            player = 2
        else:
            player = 1
        movesAvailable = MovesAvailable(board,player)
        if(movesAvailable):
            return player
        else:
            return 0

# returns the opposite of an array so the training data can be used for both players
def ReverseArray(array):
    length = len(array)
    i = 0
    while(i<length):
        array[i] = - array[i]
        i+=1
    return array