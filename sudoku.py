board = [
    [0,1,0,0,8,6,0,0,7],
    [0,0,0,0,0,4,9,0,5],
    [0,0,0,1,0,0,0,0,0],
    [0,7,0,0,5,0,0,3,2],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,9,0,7,0,0],
    [0,0,6,0,1,0,0,0,9],
    [3,4,0,0,0,0,0,0,1],
    [8,0,0,0,3,0,0,5,0]
]


def format(board):
    print("")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ",end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("")
format(board)

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None