sudoku_board = [
    [3, " ", 6, 5, " ", 8, 4, " ", " "],
    [5, 2, " ", " ", " ", " ", " ", " ", " "],
    [" ", 8, 7, " ", " ", " ", " ", 3, 1],
    [" ", " ", 3, " ", 1, " ", " ", 8, " "],
    [9, " ", " ", 8, 6, 3, " ", " ", 5],
    [" ", 5, " ", " ", 9, " ", 6, " ", " "],
    [1, 3, " ", " ", " ", " ", 2, 5, " "],
    [" "," "," "," "," "," "," ",7, 4],
    [" ", " ", 5, 2, " ", 6, 3, " ", " "]
]


def solve_sudoku(board):
    found = find_empty(board)
    if not found:
        return True
    else:
        row, column = found
     
    for i in range(1, 10):
        if validator(board, i, (row, column)):
            board[row][column] = i

            if solve_sudoku(board):
                return True
            
            board[row][column] = " "
        
    return False

        


    
def validator(board, num, pos):
    #check row first
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    #check column 
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")



def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                return (i, j) #row, col
    return None

print_board(sudoku_board)
find_empty(sudoku_board)
print(".....................................")
solve_sudoku(board = sudoku_board)
print_board(sudoku_board)