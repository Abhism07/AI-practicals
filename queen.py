import numpy as np
global n
n=int(input("Enter the shape of the board:"))
def printsolution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print()
def safety(board,row,col):
# check for the presense of any queen in a row 
    for i in range (col):
        if board[row][i] ==1:
            return False
        # for upper diagonal elements
    for i,j in zip (range (row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
        #for lower diagonal elements    
    for i,j in zip (range (row,n,1),range(col,-1,-1)):  
        if board[i][j]==1:
            return False
    return True
    
def solve(board,col):
    if col>=n:
        return True
      #Exploring board to put the queen at correct position
    for i in range(n):
    #check if the position is safe or not and then put the queen
        if safety(board,i,col):
             board[i][col]=1
             #recurse for the next possible position for new QUEEN
             if solve(board,col+1)==True:
                return True
             #If there is no solution existing for queen make it zero   
             board[i][col]=0  
    return False
    #driver code
def solution():
    '''board =[[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
          ]'''
    board = np.zeros(shape=(n,n),dtype=np.int)     
    if solve(board,0)== False:
        print("no solution exist")
        return False
    printsolution(board)
    return True            
solution()    
            
            
            
          
    
