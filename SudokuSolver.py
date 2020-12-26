from random import shuffle, randint

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
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

    numlist = [1,2,3,4,5,6,7,8,9]
    shuffle(numlist)
    for i in numlist:
        if valid(board, i, (row,col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
            
    return False

def num_solutions(board):
    if board[1] > 1:
        return False
    find = find_empty(board[0])
    if not find:
        board[1] += 1
        return False
    else:
        row, col = find

    numlist = [1,2,3,4,5,6,7,8,9]
    #shuffle(numlist)
    for i in numlist:
        if valid(board[0], i, (row,col)):
            board[0][row][col] = i
            
            if num_solutions(board):
                return True
            
            board[0][row][col] = 0
            
    return False

def remove_numbers(board, amount):
    attempts = 15
    attempts_left = attempts
    while amount > 0 and attempts_left > 0:
        row = randint(0,8)
        col = randint(0,8)
        while board[row][col] == 0:
            row = randint(0,8)
            col = randint(0,8)
        backup = board[row][col]
        board[row][col] = 0
        
        board_copy = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
            ]
        for j in range(len(board)):
            for k in range(len(board[j])):
                board_copy[j][k] = board[j][k]
                
        board_w_num_sol = [board_copy,0]
        num_solutions(board_w_num_sol)
        if board_w_num_sol[1] != 1:
            board[row][col] = backup
            attempts_left -= 1
        if board_w_num_sol[1] == 1:
            amount -= 1
            attempts_left = attempts
            
        
        

#print_board(board)
solve(board)

remove_numbers(board, 60)
print_board(board)
print("\nSolving...\n")


if(solve(board)):
    print_board(board)
else:
    print("Unsolvable")
