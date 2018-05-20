# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 16:13:32 2018

@author: Jacob
"""
def training(opponent,batches):
    import Functions
    import MachineLearning as ml
    import tensorflow as tf
    import numpy as np
    from random import random,randint
    from tensorflow.python.framework import ops
    import time
    
    ops.reset_default_graph() 
    lr = 0.0001 # the learning rate
    numInp = 65 # the number of inputs for the neural network
    numLabel = 1 # the number of inputs for the labels
    batchSize = 50 # the size of the batches
    discountRate = 0.99 # the discount rate for temporal difference learning
    
    # Create Placeholders for input and label
    inp, label = ml.placeholders(numInp, numLabel)
    
    # Initialise parameters
    parameters = ml.initialiseParameters()
    
    #make the nerual network
    out = ml.network(inp, parameters)
    
    #cost function for use in training
    cost = ml.compute_cost(out, label)
    
    #training function
    optimizer = tf.train.AdamOptimizer(learning_rate = lr).minimize(cost)
    
    player1 = "Network"
    player2 = opponent
    # Initialise all the variables
    init = tf.global_variables_initializer()
    
    progstart = time.time()
    saver = tf.train.Saver()
    expRate = 0.2
    p1wins = 0 # number of games player 1 has won overall
    p2wins = 0 # number of games player 2 has won overall
    modelPath = "./save/NetworkPlayer"#WLTD1step #testNetScore or testWinLoss
    i=1
    while i<=(batches):
        s = 1
        winLoss = np.ndarray((1,1))    
        board = Functions.BoardInit()
        boardArray = Functions.boardToNN(board,1)
        batchp1wins = 0
        batchp2wins = 0
        labelArray = np.ndarray((1,1)) 
        labelArray[0][0] = 0
        with tf.Session() as sess:
            sess.run(init)
            #loads the network in or initialises a new network
            try:
                saver.restore(sess, modelPath)
                #print("Model restored from file: %s" % modelPath)
            except:
                #sessctd = False
                print("Initializing")
            start = time.time()
            while s <= batchSize:
                movesAvailable = 1
                gamePlaying = 1
                player = randint(1,2) # returns either a 1 or a 2
                board = Functions.BoardInit()
                nnBoard = Functions.boardToNN(board,player)
                boardArray = np.concatenate((boardArray, nnBoard),axis=1)
                gameLabelArray = np.ndarray((1,1))
                while gamePlaying != 0:
                
                    while((player1 == "Network" and player == 1) and Functions.GameOver(board)==0):# if player 1 is a network
                        nextX = 0
                        nextY = 0
                        movesAvailable = Functions.MovesAvailable(board, player) # all available moves
                        bestPred = 0
                        j = 0
                        if(random()>expRate):# most of the time the network will play the move with the highest output
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
                                    if(pred>bestPred):
                                        bestPred = pred
                                        nextX = x
                                        nextY = y
                                j+=1
                        elif(movesAvailable):# sometimes the network will play a move completely randomly to better explore all possible moves
                            move = movesAvailable[randint(0,len(movesAvailable)-1)]  
                            nextX = int(move[1])
                            nextY = int(move[0])                            
                            testBoard = Functions.BoardCopy(board)
                            testBoard = Functions.MakeMove(testBoard, nextY, nextX , player)
                            bestPred = out.eval(feed_dict={inp: Functions.boardToNN(testBoard,player)})# get the output of the move
                        
                        winLoss[0][0] = bestPred*discountRate# label = output * discount rate
                        gameLabelArray = np.concatenate((gameLabelArray, winLoss),axis=1) # add the label to the list of labels
                        board = Functions.MakeMove(board, nextY , nextX , player) # update the board
                        nnBoard = Functions.boardToNN(board,player)
                        if(Functions.GameOver(board)==1): # if the game is over
                            result = Functions.BlackWhiteCount(board)#sum(nnBoard)#find the winner
                            winLoss[0][0] = result
#                            if(result>0):
#                                winLoss[0][0] = 1
#                            elif(result==0):
#                                winLoss[0][0] = 0
#                            elif(result<0):
#                                winLoss[0][0] = -1
                            # final label is equal to the winner
                            gameLabelArray = np.concatenate((gameLabelArray, winLoss),axis=1)# add the label to the list of labels
                            boardArray = np.concatenate((boardArray, nnBoard),axis=1)# add the board to the list of boards
                            #print(winLoss[0][0])
                        else:   
                            player = Functions.nextPlayer(board,player)# find who plays next
                            boardArray = np.concatenate((boardArray, nnBoard),axis=1)# add the board to the list of boards
                        
                        
                    while(((player2 == "Rand" and player == 2)) and Functions.GameOver(board)==0):# if player 2 is random
                        
                        movesAvailable = Functions.MovesAvailable(board, player)# all available moves
                        if(movesAvailable):
                            # pick and play a move at random
                            numPicked = randint(0,len(movesAvailable)-1)
                            movePicked = movesAvailable[numPicked]
                            x = int(movePicked[1])
                            y = int(movePicked[0])
                            board = Functions.MakeMove(board, y , x , player)
                            # add the resulting position to the board array and the label array
                            nnBoard = Functions.boardToNN(board,player)
                            bestPred = out.eval(feed_dict={inp:nnBoard})
                            winLoss[0][0] = bestPred*discountRate
                            gameLabelArray = np.concatenate((gameLabelArray, winLoss),axis=1)
                            if(Functions.GameOver(board)==1):# if the game is over
                                result = Functions.BlackWhiteCount(board)#sum(nnBoard)#find the winner
                                winLoss[0][0] = result
#                                if(result>0):
#                                    winLoss[0][0] = 1
#                                elif(result==0):
#                                    winLoss[0][0] = 0
#                                elif(result<0):
#                                    winLoss[0][0] = -1
                                # final label is equal to the winner
                                gameLabelArray = np.concatenate((gameLabelArray, winLoss),axis=1)# add the label to the list of labels
                                boardArray = np.concatenate((boardArray, nnBoard),axis=1)# add the board to the list of boards
                                
                        if(Functions.GameOver(board)==0):
                            player = Functions.nextPlayer(board,player)# find who plays next
                            boardArray = np.concatenate((boardArray, nnBoard),axis=1)# add the board to the list of boards
                            
                    while((player2 == "Network" and player == 2) and Functions.GameOver(board)==0):
                        nextX = 0
                        nextY = 0
                        movesAvailable = Functions.MovesAvailable(board, player) # all available moves
                        bestPred = 0
                        j = 0
                        if(random()>expRate):# most of the time the network will play the move with the highest output
                            while (j <= len(movesAvailable) - 1 and movesAvailable):# for each ove in movesAvailable
                                moveTest = movesAvailable[j]    
                                x = int(moveTest[1])
                                y = int(moveTest[0])
                                testBoard = Functions.BoardCopy(board)
                                testBoard = Functions.MakeMove(testBoard, y , x , player)
                                
                                pred = out.eval(feed_dict={inp: Functions.boardToNN(testBoard,player)})# get the output of an available move
                                
                                #finds the move with the lowest output, output of -1 means player 2 is guaranteed to win
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
                        elif(movesAvailable):# sometimes the network will play a move completely randomly to better explore all possible moves
                            move = movesAvailable[randint(0,len(movesAvailable)-1)]  
                            nextX = int(move[1])
                            nextY = int(move[0])                            
                            testBoard = Functions.BoardCopy(board)
                            testBoard = Functions.MakeMove(testBoard, nextY, nextX , player)
                            bestPred = out.eval(feed_dict={inp: Functions.boardToNN(testBoard,player)})# get the output of the move
                        
                        winLoss[0][0] = bestPred*discountRate# label = output * discount rate
                        gameLabelArray = np.concatenate((gameLabelArray, winLoss),axis=1) # add the label to the list of labels
                        board = Functions.MakeMove(board, nextY , nextX , player) # update the board
                        nnBoard = Functions.boardToNN(board,player)
                        if(Functions.GameOver(board)==1): # if the game is over
                            result = Functions.BlackWhiteCount(board)#sum(nnBoard)#find the winner
                            winLoss[0][0] = result
#                            if(result>0):
#                                winLoss[0][0] = 1
#                            elif(result==0):
#                                winLoss[0][0] = 0
#                            elif(result<0):
#                                winLoss[0][0] = -1
                            # final label is equal to the winner
                            gameLabelArray = np.concatenate((gameLabelArray, winLoss),axis=1)# add the label to the list of labels
                            boardArray = np.concatenate((boardArray, nnBoard),axis=1)# add the board to the list of boards
                            #print(winLoss[0][0])
                        else:   
                            player = Functions.nextPlayer(board,player)# find who plays next
                            boardArray = np.concatenate((boardArray, nnBoard),axis=1)# add the board to the list of boards
                        
                            
                    if(Functions.GameOver(board)==1):#if the game ends
                        concArray = np.copy(gameLabelArray[0][1:])# copy all the data from the array of labels
                        size = len(concArray)
                        concArray = np.reshape(concArray,(1,size))
                        """
                        reshape the array and remove the first value, 
                        this means the label for the first board state is equal to the output of the next move * the discount rate
                        """
                        labelArray = np.concatenate((labelArray, concArray),axis = 1)
                        gamePlaying = 0
                        Winner = Functions.BlackWhiteCount(board)#sum(nnBoard)
                        if(Winner > 0):
                            batchp1wins+=1
                            p1wins+=1
                        elif(Winner < 0):
                            batchp2wins+=1
                            p2wins+=1
                s+=1
            print("batch: ",i," out of ", batches)
            
            print("player 1 (", player1, ") wins " ,batchp1wins)
            print("player 2 (", player2, ") wins " ,batchp2wins)
            
            """
            the following code flips the training data since a position where player 2 is guaranteed to win 
            would be a position where player 1 is guaranteed to win if every piece was reversed
            """
            labelArrayOpp = Functions.ReverseArray(labelArray)
            boardArrayOpp = Functions.ReverseArray(boardArray)
            labelArray = np.concatenate((labelArray,labelArrayOpp),axis = 1)
            boardArray = np.concatenate((boardArray,boardArrayOpp),axis = 1)
            
            #trains the neural network
            _ , boardCost = sess.run([optimizer, cost], feed_dict={inp: boardArray, label: labelArray})
            print(boardCost)
            #savePath = saver.save(sess, modelPath)# saves the updated network
            end = time.time()
            print("batch time(secs) ",end-start)
        
        i+=1
                    
    progend = time.time()
    print("total games: ",batches*batchSize)
    print("player 1 (", player1, ") wins " ,p1wins)
    print("player 2 (", player2, ") wins " ,p2wins)
    print("total time(secs) ",progend-progstart)   