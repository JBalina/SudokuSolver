board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end="")
                    
                    
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

#Check if current numbers works
def valid(board,num,pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    sectX = int(pos[1]/3)
    sectY = int(pos[0]/3)
    
    for i in range(sectY*3, sectY*3 + 3):
        for j in range(sectX*3, sectX*3 +3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True
        
#Recursively check options to find solution
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
            
    return False

print_board(board)

solve(board)
print("")
print_board(board)