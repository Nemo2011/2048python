# The Core

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
EMPTY_BOARD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ALL_TWO_BOARD = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

def is_real(board:list) -> bool:
    """ Check the real of the board """
    if len(board) != 16:
        return False
    for num in board:
        lst = (0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048)
        if not num in lst:
            return False
    return True

def is_2048(board:list) -> bool:
    """ Check 2048 in the board. """
    bool = is_real(board)
    if bool == False:
        raise ValueError("The board is not real.")
    bool = (2048 in board)
    return bool

def can_move(board:list) -> bool:
    """ Check the board, return can the board move. """
    zero = board.count(0)
    if zero > 0:
        return True
    line_list = [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    for line in line_list:
        for x in range(3):
            if board[line[x]] == board[line[x + 1]]:
                return True
    return False

def move(board:list, mode:int) -> list:
    """ Move the board. the mode was a number, if is 0, the board move up, 1 then move down, 
    2 then move left, 3 then move right, return the board and is the board merge """
    is_r = is_real(board)
    if is_r == False:
        raise ValueError("The board is not real.")
    if mode == 0:
        line_list = [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]
    elif mode == 1:
        line_list = [[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]]
    elif mode == 2:
        line_list = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    elif mode == 3:
        line_list = [[3, 2, 1, 0], [7, 6, 5, 4], [11, 10, 9, 8], [15, 14, 13, 12]]
    merge = False
    for line in line_list:
        new_list = []
        for index in line:
            if board[index] != 0:
                new_list.append(board[index])
        while len(new_list) != 4:
            new_list.append(0)
        for index in range(len(new_list) - 1):
            if new_list[index] == new_list[index + 1]:
                if new_list[index] != 0:
                    merge = True
                new_list[index] *= 2
                new_list[index + 1] = 0
                for i in range(index + 1, len(new_list) - 1):
                    new_list[i] = new_list[i + 1]
                    new_list[i + 1] = 0
        for x in range(4):
            board[line[x]] = new_list[x]
    return [board, merge]

if __name__ == '__main__':
    print(can_move([8, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 8, 2, 4, 8]))
    print(move([2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], DOWN))
    print(move(ALL_TWO_BOARD, LEFT))