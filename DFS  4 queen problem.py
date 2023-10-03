
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E', 'F'],
    'D': ['G', 'B'],
    'E': ['B', 'C'],
    'F': ['C', 'H'],
    'G': ['I'],
    'I':['J'],
    'J':[],
    'H': ['K'],
    'K': ['L'],
    'L': ['M'],
    'M': ['N'],
    'N':[]
}
lable={
       'A':[0,0],
       'B':[0,3],
       'C':[4,0],
       'D':[3,0],
       'E':[4,3],
       'F':[1,3],
       'G':[3,3],
       'H':[1,0],
       'I':[4,2],
       'J':[0,2],
       'K':[0,1],
       'L':[4,1],
       'M':[2,3],
       'N':[2,0],
       }

def is_safe(board, row, col):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True
    
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    
    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def solve_4_queens():
    board = [[0 for _ in range(4)] for _ in range(4)]
    
    if not solve_n_queens(board, 0):
        print("No solution exists.")
        return
    
    print_solution(board)

if __name__ == "__main__":
    solve_4_queens()
