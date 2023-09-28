import random
from config import WHITE_SPACE, BOARD_ROW, BOARD_COL
from entities.board import Board

def get_index_in_final_board(cell: int):
    if not cell or cell >= BOARD_ROW * BOARD_COL:
        raise Exception("212")

    index = cell - 1
    return index // BOARD_COL, index % BOARD_COL


def manhattan(board_matrix):
    value = 0

    for board_row, ROW in enumerate(board_matrix):
        for board_col, cell in enumerate(ROW):
            if cell == WHITE_SPACE:
                continue

            final_board_row, final_board_col = get_index_in_final_board(cell)
            value += abs(board_row - final_board_row) + abs(board_col - final_board_col)

    return value




def out_of_place(board_matrix):
    value = 0

    for board_row, ROW in enumerate(board_matrix):
        for board_col, cell in enumerate(ROW):
            if cell == WHITE_SPACE:
                continue

            final_board_row, final_board_col = get_index_in_final_board(cell)
            d = abs(board_row - final_board_row) + abs(board_col - final_board_col)
            value += 0 if d == 0 else 1

    return value


heuristic = {
    "manhattan": manhattan,
    "out_of_place": out_of_place
}


def generate_final_board():
    last_index_row = BOARD_ROW - 1
    last_index_col = BOARD_COL - 1

    matrix = []
    for row in range(0, BOARD_ROW):
        matrix.append([])
        for col in range(0, BOARD_COL):
            cell = (row * BOARD_COL) + col + 1
            matrix[row].append(cell)
    
    matrix[last_index_row][last_index_col] = WHITE_SPACE
    return matrix

def generate_initial_board(final_board: "Board", MOVES = 50):
    BOARD_PASSED = [final_board]
    current_board = final_board
    
    moves = 0
    for m in range(0, MOVES):
        
        boards = [ board for board in current_board.next_boards() if board not in BOARD_PASSED ]
        for board in boards:
            BOARD_PASSED.append(board)

        if len(boards) == 0:
            break
        
        moves += 1
        board = random.choice(boards)
        current_board = board

    
    print(f"Realizado {moves} movimentos")
    
    return current_board