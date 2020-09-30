import random

orig_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,None]]


def create_shuffled_board(orig_board):
    """Create the 4x4 board and Shuffle the board into a valid starting position
        returns: board (list of lists)"""
    for i in range(50):
        #get a random move (up, down, left right)
        num = random.choice("wasd")
        #no need to write as an explicit list
        #['w','a','s','d'])
        #use the move function to randomly move the tiles
        board = move_tile(orig_board,num, display_invalid=False)
    return board

#board = create_shuffled_board(orig_board)
def move_tile(board, move, display_invalid=True):
    new_board = board
    size = len(board) # default is 4
    if move not in "WASDwasd":
        return board
    r, c = find_tile(board, tile=None)
    if move in "Ss" and r > 0:
        new_board[r][c] = board[r-1][c]
        new_board[r-1][c] = None
    elif move in "Ww" and r < size-1:
        new_board[r][c] = board[r+1][c]
        new_board[r+1][c] = None
    elif move in "Dd" and c > 0:
        new_board[r][c] = board[r][c-1]
        new_board[r][c-1] = None
    elif move in "Aa" and c < size-1:
        new_board[r][c] = board[r][c+1]
        new_board[r][c+1] = None
    else:
        if display_invalid:
            print("Invalid move.")
    return new_board
    

def find_tile(board, tile=None):
    # Find row with tile
    r = [i for i, row in enumerate(board) if tile in row][0]
    # Find position of tile within that row
    c = board[r].index(tile)
    # Return coordinates of tile
    return r, c
    
    
def check_win(board):
    return board == [[1, 2, 3, 4   ],
                     [5, 6, 7, 8   ],
                     [9, 10,11,12  ],
                     [13,14,15,None]]
    
def print_board(board):
    ans_str = ""
    for row in board:
        for column in row:
            if not column:
                # more Pythonic than "== None"
                column = "__"
            ans_str += str(column).rjust(2, " ") + " "
        ans_str += "\n"

    print(ans_str)


size = 4

game_won = False
game_board = create_shuffled_board(orig_board)

while not game_won:
    print_board(game_board)
    move = input("Please enter a move:\n")
    # if not validate_move(game_board, move):
        # print("move not valid")
        # continue
    board = move_tile(game_board, move)
    game_won = check_win(game_board)

print_board(game_board)
print("You won!")