# in this we will be creating a function to solve a sudoku puzzle
# in this basically we will be using recurssion to solve it

# with the help of find_next_empty function, we are findind an empty position in the puzzle
# for this we are iterating row and column
# -1 stands for , the space is empty, or it denotes an empty place
# and if an empty place is found replace it with r,c
from pprint import pprint
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None

# now with the help of is_valid function, we are identifying that our choice is valid or not
# it will check all the rows and columns for identical characters
# if any identical character is found , then that is invelid..

def is_valid(puzzle,guess,row,col):
    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    col_vals=[]
    for i in range(9):
        col_vals.append(puzzle[i][col])
        if guess in col_vals:
            return False
        
    row_start=(row//3)*3
    col_start=(col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    return True
        
def solve_sudoku(puzzle):
    row,col=find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col]=-1
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
    