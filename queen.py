import numpy as np

def printsolution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def safety(board, row, col):
    # Check for the presence of any queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal elements
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal elements
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col):
    if col >= n:
        return True

    # Sort rows based on the number of conflicts with queens in previous columns
    sorted_rows = sorted(range(n), key=lambda row: sum(board[row][:col]))

    for row in sorted_rows:
        if safety(board, row, col):
            board[row][col] = 1
            if solve(board, col + 1):
                return True
            board[row][col] = 0
    return False

def solution():
    board = np.zeros(shape=(n, n), dtype=np.int64)
    if solve(board, 0) == False:
        print("No solution exists.")
        return False
    printsolution(board)
    return True

# Driver code
n = int(input("Enter the shape of the board:"))
solution()

'''
o/p-
G:\Ai programs>python br_bound.py
Enter the shape of the board:5
1 0 0 0 0
0 0 0 1 0
0 1 0 0 0
0 0 0 0 1
0 0 1 0 0

G:\Ai programs>python br_bound.py
Enter the shape of the board:8
1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 1
0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 0 0 1 0 0
0 0 1 0 0 0 0 0
'''
