import copy

WHITE_SPACE = None
BOARD_FINAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, WHITE_SPACE]
]




class Board:


    def __init__(self, matrix, euristik) -> None:
        pass


def get_index_in_board_final(cell: int):
    index = cell - 1
    return index // 3, index % 3


def manhattan(board):
    value = 0

    for board_row, ROW in enumerate(board):
        for board_col, cell in enumerate(ROW):
            if cell == WHITE_SPACE:
                continue

            board_final_row, board_final_col = get_index_in_board_final(cell)
            value += abs(board_row - board_final_row) + abs(board_col - board_final_col)


    return value


board = [
    [7, 8, 6],
    [1, 3, 2],
    [5, 4, WHITE_SPACE]
]

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def generate_options(board):
    position_row = None
    position_col = None

    for board_row, ROW in enumerate(board):
        for board_col, cell in enumerate(ROW):
            if cell == WHITE_SPACE:
                position_row = board_row
                position_col = board_col

                break

        if position_col is not None:
            break

    boards = []
    for row, col in DIRECTIONS:
        new_position_row = position_row + row
        new_position_col = position_col + col

        if (new_position_row >= len(BOARD_FINAL) or new_position_row < 0):
            continue

        if (new_position_col >= len(BOARD_FINAL[0]) or new_position_col < 0):
            continue

        new_board = copy.deepcopy(board)

        tmp = new_board[position_row][position_col]
        new_board[position_row][position_col] = new_board[new_position_row][new_position_col]
        new_board[new_position_row][new_position_col] = tmp

        boards.append(new_board)

    return boards

board_passed = []

print(BOARD_FINAL in [copy.deepcopy(BOARD_FINAL)])
        
current_board = board
board_passed.append(board)
while not manhattan(current_board) == 0:
    boards = generate_options(current_board)
    boards = [x for x in boards if x not in board_passed]
    lower_board = None
    for board in boards:
        if lower_board is None:
            lower_board = board
            continue

        lower_board = board if manhattan(board) < manhattan(lower_board) else lower_board

    print(lower_board)
    current_board = lower_board
    board_passed.append(lower_board)  


# for x in list_boards:
#     print(x)



# print(manhattan(board))

print(generate_options(board))