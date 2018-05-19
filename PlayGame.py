'''
Created on 18 Feb 2018

@author: Jacob
'''
import MachineLearning as ml
import tkinter
import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops
import Functions
import time
from random import randint
import Training
global board
board = Functions.BoardInit()
player = 1
#window = tkinter.Tk()
 # the function called when the player makes a move
def Move(x,y,player):
    global board
    #if the move is legal
    if(Functions.TryMove(board, y, x, player)==1):
        #update the board
        board = Functions.MakeMove(board, y , x , player)
        #update the player
        player = Functions.nextPlayer(board,player)
        #if it's the opponents turn allow them to make a move
        UpdateBoard(player)
        cont.set(1)
        time.sleep(0.25)
            
def UpdateBoard(player):
    global board
    #converts the board numbers into colours
    colourBoard = Functions.BoardtoColour(board)
    #makes a button for each board tile
    window.button00 = tkinter.Button(window,height=1,width=1,command = lambda:Move(0,0,player),bg = colourBoard[0][0])
    window.button01 = tkinter.Button(window,height=1,width=1,command = lambda:Move(0,1,player),bg = colourBoard[0][1])
    window.button02 = tkinter.Button(window,height=1,width=1,command = lambda:Move(0,2,player),bg = colourBoard[0][2])
    window.button03 = tkinter.Button(window,height=1,width=1,command = lambda:Move(0,3,player),bg = colourBoard[0][3])
    window.button04 = tkinter.Button(window,height=1,width=1,command = lambda:Move(0,4,player),bg = colourBoard[0][4])
    window.button05 = tkinter.Button(window,height=1,width=1,command = lambda:Move(0,5,player),bg = colourBoard[0][5])
    window.button06 = tkinter.Button(window,height=1,width=1,command = lambda:Move(0,6,player),bg = colourBoard[0][6])
    window.button07 = tkinter.Button(window,height=1,width=1,command = lambda:Move(0,7,player),bg = colourBoard[0][7])
    window.button00.grid(row = 1,column = 1)
    window.button01.grid(row = 1,column = 2)
    window.button02.grid(row = 1,column = 3)
    window.button03.grid(row = 1,column = 4)
    window.button04.grid(row = 1,column = 5)
    window.button05.grid(row = 1,column = 6)
    window.button06.grid(row = 1,column = 7)
    window.button07.grid(row = 1,column = 8)
    
    window.button10 = tkinter.Button(window,height=1,width=1,command = lambda:Move(1,0,player),bg = colourBoard[1][0])
    window.button11 = tkinter.Button(window,height=1,width=1,command = lambda:Move(1,1,player),bg = colourBoard[1][1])
    window.button12 = tkinter.Button(window,height=1,width=1,command = lambda:Move(1,2,player),bg = colourBoard[1][2])
    window.button13 = tkinter.Button(window,height=1,width=1,command = lambda:Move(1,3,player),bg = colourBoard[1][3])
    window.button14 = tkinter.Button(window,height=1,width=1,command = lambda:Move(1,4,player),bg = colourBoard[1][4])
    window.button15 = tkinter.Button(window,height=1,width=1,command = lambda:Move(1,5,player),bg = colourBoard[1][5])
    window.button16 = tkinter.Button(window,height=1,width=1,command = lambda:Move(1,6,player),bg = colourBoard[1][6])
    window.button17 = tkinter.Button(window,height=1,width=1,command = lambda:Move(1,7,player),bg = colourBoard[1][7])
    window.button10.grid(row = 2,column = 1)
    window.button11.grid(row = 2,column = 2)
    window.button12.grid(row = 2,column = 3)
    window.button13.grid(row = 2,column = 4)
    window.button14.grid(row = 2,column = 5)
    window.button15.grid(row = 2,column = 6)
    window.button16.grid(row = 2,column = 7)
    window.button17.grid(row = 2,column = 8)
        
    window.button20 = tkinter.Button(window,height=1,width=1,command = lambda:Move(2,0,player),bg = colourBoard[2][0])
    window.button21 = tkinter.Button(window,height=1,width=1,command = lambda:Move(2,1,player),bg = colourBoard[2][1])
    window.button22 = tkinter.Button(window,height=1,width=1,command = lambda:Move(2,2,player),bg = colourBoard[2][2])
    window.button23 = tkinter.Button(window,height=1,width=1,command = lambda:Move(2,3,player),bg = colourBoard[2][3])
    window.button24 = tkinter.Button(window,height=1,width=1,command = lambda:Move(2,4,player),bg = colourBoard[2][4])
    window.button25 = tkinter.Button(window,height=1,width=1,command = lambda:Move(2,5,player),bg = colourBoard[2][5])
    window.button26 = tkinter.Button(window,height=1,width=1,command = lambda:Move(2,6,player),bg = colourBoard[2][6])
    window.button27 = tkinter.Button(window,height=1,width=1,command = lambda:Move(2,7,player),bg = colourBoard[2][7])
    window.button20.grid(row = 3,column = 1)
    window.button21.grid(row = 3,column = 2)
    window.button22.grid(row = 3,column = 3)
    window.button23.grid(row = 3,column = 4)
    window.button24.grid(row = 3,column = 5)
    window.button25.grid(row = 3,column = 6)
    window.button26.grid(row = 3,column = 7)
    window.button27.grid(row = 3,column = 8)
        
    window.button30 = tkinter.Button(window,height=1,width=1,command = lambda:Move(3,0,player),bg = colourBoard[3][0])
    window.button31 = tkinter.Button(window,height=1,width=1,command = lambda:Move(3,1,player),bg = colourBoard[3][1])
    window.button32 = tkinter.Button(window,height=1,width=1,command = lambda:Move(3,2,player),bg = colourBoard[3][2])
    window.button33 = tkinter.Button(window,height=1,width=1,command = lambda:Move(3,3,player),bg = colourBoard[3][3])
    window.button34 = tkinter.Button(window,height=1,width=1,command = lambda:Move(3,4,player),bg = colourBoard[3][4])
    window.button35 = tkinter.Button(window,height=1,width=1,command = lambda:Move(3,5,player),bg = colourBoard[3][5])
    window.button36 = tkinter.Button(window,height=1,width=1,command = lambda:Move(3,6,player),bg = colourBoard[3][6])
    window.button37 = tkinter.Button(window,height=1,width=1,command = lambda:Move(3,7,player),bg = colourBoard[3][7])
    window.button30.grid(row = 4,column = 1)
    window.button31.grid(row = 4,column = 2)
    window.button32.grid(row = 4,column = 3)
    window.button33.grid(row = 4,column = 4)
    window.button34.grid(row = 4,column = 5)
    window.button35.grid(row = 4,column = 6)
    window.button36.grid(row = 4,column = 7)
    window.button37.grid(row = 4,column = 8)
    
    window.button40 = tkinter.Button(window,height=1,width=1,command = lambda:Move(4,0,player),bg = colourBoard[4][0])
    window.button41 = tkinter.Button(window,height=1,width=1,command = lambda:Move(4,1,player),bg = colourBoard[4][1])
    window.button42 = tkinter.Button(window,height=1,width=1,command = lambda:Move(4,2,player),bg = colourBoard[4][2])
    window.button43 = tkinter.Button(window,height=1,width=1,command = lambda:Move(4,3,player),bg = colourBoard[4][3])
    window.button44 = tkinter.Button(window,height=1,width=1,command = lambda:Move(4,4,player),bg = colourBoard[4][4])
    window.button45 = tkinter.Button(window,height=1,width=1,command = lambda:Move(4,5,player),bg = colourBoard[4][5])
    window.button46 = tkinter.Button(window,height=1,width=1,command = lambda:Move(4,6,player),bg = colourBoard[4][6])
    window.button47 = tkinter.Button(window,height=1,width=1,command = lambda:Move(4,7,player),bg = colourBoard[4][7])
    window.button40.grid(row = 5,column = 1)
    window.button41.grid(row = 5,column = 2)
    window.button42.grid(row = 5,column = 3)
    window.button43.grid(row = 5,column = 4)
    window.button44.grid(row = 5,column = 5)
    window.button45.grid(row = 5,column = 6)
    window.button46.grid(row = 5,column = 7)
    window.button47.grid(row = 5,column = 8)
    
    window.button50 = tkinter.Button(window,height=1,width=1,command = lambda:Move(5,0,player),bg = colourBoard[5][0])
    window.button51 = tkinter.Button(window,height=1,width=1,command = lambda:Move(5,1,player),bg = colourBoard[5][1])
    window.button52 = tkinter.Button(window,height=1,width=1,command = lambda:Move(5,2,player),bg = colourBoard[5][2])
    window.button53 = tkinter.Button(window,height=1,width=1,command = lambda:Move(5,3,player),bg = colourBoard[5][3])
    window.button54 = tkinter.Button(window,height=1,width=1,command = lambda:Move(5,4,player),bg = colourBoard[5][4])
    window.button55 = tkinter.Button(window,height=1,width=1,command = lambda:Move(5,5,player),bg = colourBoard[5][5])
    window.button56 = tkinter.Button(window,height=1,width=1,command = lambda:Move(5,6,player),bg = colourBoard[5][6])
    window.button57 = tkinter.Button(window,height=1,width=1,command = lambda:Move(5,7,player),bg = colourBoard[5][7])
    window.button50.grid(row = 6,column = 1)
    window.button51.grid(row = 6,column = 2)
    window.button52.grid(row = 6,column = 3)
    window.button53.grid(row = 6,column = 4)
    window.button54.grid(row = 6,column = 5)
    window.button55.grid(row = 6,column = 6)
    window.button56.grid(row = 6,column = 7)
    window.button57.grid(row = 6,column = 8)
        
    window.button60 = tkinter.Button(window,height=1,width=1,command = lambda:Move(6,0,player),bg = colourBoard[6][0])
    window.button61 = tkinter.Button(window,height=1,width=1,command = lambda:Move(6,1,player),bg = colourBoard[6][1])
    window.button62 = tkinter.Button(window,height=1,width=1,command = lambda:Move(6,2,player),bg = colourBoard[6][2])
    window.button63 = tkinter.Button(window,height=1,width=1,command = lambda:Move(6,3,player),bg = colourBoard[6][3])
    window.button64 = tkinter.Button(window,height=1,width=1,command = lambda:Move(6,4,player),bg = colourBoard[6][4])
    window.button65 = tkinter.Button(window,height=1,width=1,command = lambda:Move(6,5,player),bg = colourBoard[6][5])
    window.button66 = tkinter.Button(window,height=1,width=1,command = lambda:Move(6,6,player),bg = colourBoard[6][6])
    window.button67 = tkinter.Button(window,height=1,width=1,command = lambda:Move(6,7,player),bg = colourBoard[6][7])
    window.button60.grid(row = 7,column = 1)
    window.button61.grid(row = 7,column = 2)
    window.button62.grid(row = 7,column = 3)
    window.button63.grid(row = 7,column = 4)
    window.button64.grid(row = 7,column = 5)
    window.button65.grid(row = 7,column = 6)
    window.button66.grid(row = 7,column = 7)
    window.button67.grid(row = 7,column = 8)
        
    window.button70 = tkinter.Button(window,height=1,width=1,command = lambda:Move(7,0,player),bg = colourBoard[7][0])
    window.button71 = tkinter.Button(window,height=1,width=1,command = lambda:Move(7,1,player),bg = colourBoard[7][1])
    window.button72 = tkinter.Button(window,height=1,width=1,command = lambda:Move(7,2,player),bg = colourBoard[7][2])
    window.button73 = tkinter.Button(window,height=1,width=1,command = lambda:Move(7,3,player),bg = colourBoard[7][3])
    window.button74 = tkinter.Button(window,height=1,width=1,command = lambda:Move(7,4,player),bg = colourBoard[7][4])
    window.button75 = tkinter.Button(window,height=1,width=1,command = lambda:Move(7,5,player),bg = colourBoard[7][5])
    window.button76 = tkinter.Button(window,height=1,width=1,command = lambda:Move(7,6,player),bg = colourBoard[7][6])
    window.button77 = tkinter.Button(window,height=1,width=1,command = lambda:Move(7,7,player),bg = colourBoard[7][7])
    window.button70.grid(row = 8,column = 1)
    window.button71.grid(row = 8,column = 2)
    window.button72.grid(row = 8,column = 3)
    window.button73.grid(row = 8,column = 4)
    window.button74.grid(row = 8,column = 5)
    window.button75.grid(row = 8,column = 6)
    window.button76.grid(row = 8,column = 7)
    window.button77.grid(row = 8,column = 8)
        
        
    window.update_idletasks()
    #window.update()
        
def PlayGame(opponent):
    global board
    board = Functions.BoardInit()
    player = 1
    UpdateBoard(player)
    if(opponent == "Human"):
            
        player = randint(1,2)
        movesAvailable = 1
        gamePlaying = 1
        while gamePlaying != 0:
            
            if(Functions.GameOver(board)==1):
                gamePlaying = 0
                score = Functions.BlackWhiteCount(board)
                if(score>0):
                    winner = 1
                elif(score<0):
                    winner = 2
                else:
                    winner = 0
                if(winner!=0):
                    print("Game Over! The winner is player ",winner)
                else:
                    print("It's a tie!")
                    
                board = Functions.BoardInit()
            
            cont.set(0)
            window.wait_variable(cont)
            player = Functions.nextPlayer(board,player)
            
            time.sleep(0.25)
    if(opponent == "Rand"):
        while Functions.GameOver(board)==0:
            
            player = randint(1,2)
            movesAvailable = 1
            gamePlaying = 1
            while gamePlaying != 0:
                UpdateBoard(player)
                    
                if(Functions.GameOver(board)==1):
                        gamePlaying = 0
                        score = Functions.BlackWhiteCount(board)
                        if(score>0):
                            winner = 1
                        elif(score<0):
                            winner = 2
                        else:
                            winner = 0
                        if(winner!=0):
                            print("Game Over! The winner is player ",winner)
                        else:
                            print("It's a tie!")
                        
                        board = Functions.BoardInit()
                movesAvailable = Functions.MovesAvailable(board, player)
                
                cont.set(0)
                if(player == 1):
                    window.wait_variable(cont)
                player = Functions.nextPlayer(board,player)
                
                
                time.sleep(0.25)
                while(player == 2):
                    movesAvailable = Functions.MovesAvailable(board, player)
                    print("movesAvailable",movesAvailable)
                    if(movesAvailable):
                        numPicked = randint(0,len(movesAvailable)-1)
                        print("numPicked",numPicked)
                        movePicked = movesAvailable[numPicked]
                        print("movePicked from movesAvailable",movePicked[0],movePicked[1])
                        x = int(movePicked[1])
                        y = int(movePicked[0])
                        board = Functions.MakeMove(board, y , x , player)
                    player = Functions.nextPlayer(board,player)
                    
    elif(opponent == "MinMax"):
        while Functions.GameOver(board)==0:
            
            player = randint(1,2)
            UpdateBoard(player);
            movesAvailable = 1
            gamePlaying = 1
            while gamePlaying != 0:
                UpdateBoard(player)
                    
                if(Functions.GameOver(board)==1):
                        gamePlaying = 0
                        score = Functions.BlackWhiteCount(board)
                        if(score>0):
                            winner = 1
                        elif(score<0):
                            winner = 2
                        else:
                            winner = 0
                        if(winner!=0):
                            print("Game Over! The winner is player ",winner)
                        else:
                            print("It's a tie!")
                        
                        board = Functions.BoardInit()
                movesAvailable = Functions.MovesAvailable(board, player)
                
                cont.set(0)
                if(player == 1):
                    window.wait_variable(cont)
                player = Functions.nextPlayer(board,player)
                
                
                time.sleep(0.25)
                while(player == 2):
                        nextX = 0
                        nextY = 0
                        movesAvailable = Functions.MovesAvailable(board, player) # all available moves
                        bestPred = 0
                        j = 0
                        while (j <= len(movesAvailable) - 1 and movesAvailable):# for each ove in movesAvailable
                            moveTest = movesAvailable[j]    
                            x = int(moveTest[1])
                            y = int(moveTest[0])
                            testBoard = Functions.BoardCopy(board)
                            testBoard = Functions.MakeMove(testBoard, y , x , player)
                            
                            pred = np.sum(Functions.boardToNN(testBoard,player))# get the output of an available move
                            
                            #finds the move with the highest output, output of 1 means player 1 is guaranteed to win
                            if(j == 0):
                                bestPred = pred
                                nextX = x
                                nextY = y
                            else:
                                if(pred<bestPred):
                                    bestPred = pred
                                    nextX = x
                                    nextY = y
                            j+=1
                        board = Functions.MakeMove(board, nextY , nextX , player)
                        player = Functions.nextPlayer(board,player)
    elif(opponent == "Network"):
        ops.reset_default_graph() 
        numInp = 65 # the number of inputs for the neural network
        numLabel = 1 # the number of inputs for the labels
        
        # Create Placeholders for input and label
        inp, label = ml.placeholders(numInp, numLabel)
        
        # Initialize parameters
        parameters = ml.initializeParameters()
        
        #make the nerual network
        out = ml.network(inp, parameters)
        
        modelPath = "./save/Network"
        # Initialize all the variables
        init = tf.global_variables_initializer()
        
        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(init)
            #loads the network in or initialises a new network
            try:
                saver.restore(sess, modelPath)
                #print("Model restored from file: %s" % modelPath)
            except:
                #sessctd = False
                print("Initializing")
            while Functions.GameOver(board)==0:
                
                board = Functions.BoardInit()
                player = randint(1,2)
                UpdateBoard(player);
                movesAvailable = 1
                gamePlaying = 1
                while gamePlaying != 0:
                    UpdateBoard(player)
                        
                    if(Functions.GameOver(board)==1):
                        gamePlaying = 0
                        score = Functions.BlackWhiteCount(board)
                        if(score>0):
                            winner = 1
                        elif(score<0):
                            winner = 2
                        else:
                            winner = 0
                        if(winner!=0):
                            print("Game Over! The winner is player ",winner)
                        else:
                            print("It's a tie!")
                        
                        board = Functions.BoardInit()
                    movesAvailable = Functions.MovesAvailable(board, player)
                    
                    
                    cont.set(0)
                    if(player == 1):
                        window.wait_variable(cont)
                    player = Functions.nextPlayer(board,player)
                    
                    
                    time.sleep(0.25)
                    while(player == 2):
                        nextX = 0
                        nextY = 0
                        movesAvailable = Functions.MovesAvailable(board, player) # all available moves
                        bestPred = 0
                        j = 0
                        while (j <= len(movesAvailable) - 1 and movesAvailable):# for each ove in movesAvailable
                            moveTest = movesAvailable[j]    
                            x = int(moveTest[1])
                            y = int(moveTest[0])
                            testBoard = Functions.BoardCopy(board)
                            testBoard = Functions.MakeMove(testBoard, y , x , player)
                            
                            pred = out.eval(feed_dict={inp: Functions.boardToNN(testBoard,player)})# get the output of an available move
                            
                            #finds the move with the highest output, output of 1 means player 1 is guaranteed to win
                            if(j == 0):
                                bestPred = pred
                                nextX = x
                                nextY = y
                            else:
                                if(pred<bestPred):
                                    bestPred = pred
                                    nextX = x
                                    nextY = y
                            j+=1
                        board = Functions.MakeMove(board, nextY , nextX , player)
                        player = Functions.nextPlayer(board,player)
                        
window = tkinter.Tk()
#frame = tkinter.Frame(window)
#frame.pack()
window.buttonNetwork = tkinter.Button(window,text = "Network",command = lambda:PlayGame("Network"))
window.buttonNetwork.grid(row = 1)

window.buttonHuman = tkinter.Button(window,text = "Human",command = lambda:PlayGame("Human"))
window.buttonHuman.grid(row = 2)

window.buttonMinMax = tkinter.Button(window,text = "MinMax",command = lambda:PlayGame("MinMax"))
window.buttonMinMax.grid(row = 3)

window.buttonRand = tkinter.Button(window,text="Random Game",command=lambda:PlayGame("Rand"))
window.buttonRand.grid(row = 5)

window.buttonTrain = tkinter.Button(window,text = "Train Network",command = lambda:Training.training("Network",100000))
window.buttonTrain.grid(row = 7)

window.buttonEnd = tkinter.Button(window,text = "Exit",command = window.destroy)
window.buttonEnd.grid(row = 8)
UpdateBoard(player)

cont = tkinter.IntVar()
window.mainloop()