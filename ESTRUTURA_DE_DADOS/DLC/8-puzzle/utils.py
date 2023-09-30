import random
from config import WHITE_SPACE, BOARD_ROW, BOARD_COL
from entities.board import Board


def generate_initial_board(final_board: "Board", MOVEMENTS = 50):
    BOARD_PASSED = [final_board]
    current_board = final_board
    
    movements = 0
    for _m in range(0, MOVEMENTS):
        
        boards = [ board for board in current_board.next_boards() if board not in BOARD_PASSED ]
        for board in boards:
            BOARD_PASSED.append(board)

        if len(boards) == 0:
            break
        
        movements += 1
        board = random.choice(boards)
        current_board = board

    
    print(f"Realizado {movements} movimentos")
    
    return current_board



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



CACHE_POSITION_MATRIX_FINAL_BOARD = {}
MATRIX_FINAL_BOARD = generate_final_board()
# MATRIX_FINAL_BOARD = [
#     ["_", 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]

for board_row, ROW in enumerate(MATRIX_FINAL_BOARD):
    for board_col, cell in enumerate(ROW):
        CACHE_POSITION_MATRIX_FINAL_BOARD[cell] = board_row, board_col



class GetIndexInFinalBoardException(Exception):
    pass


def get_index_in_final_board(cell: int):
    position = CACHE_POSITION_MATRIX_FINAL_BOARD.get(cell, None)
    if position is None:
        raise GetIndexInFinalBoardException("Não foi possível obter o índice do board final.")

    return position


