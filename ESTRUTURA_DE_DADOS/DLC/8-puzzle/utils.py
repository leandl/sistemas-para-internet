import random
from config import WHITE_SPACE, BOARD_ROW, BOARD_COL
from entities.board import Board


def generate_initial_board(final_board: "Board", MOVEMENTS = 50):
    BOARD_PASSED = [final_board]
    current_board = final_board
    
    movements = 0
    for _m in range(0, MOVEMENTS):
        
        boards = [ board for board in current_board.next_boards() if board not in BOARD_PASSED ]
        

        if len(boards) == 0:
            break
        
        board = random.choice(boards)
        BOARD_PASSED.append(board)
        current_board = board
        movements += 1

    
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


<<<<<<< HEAD
=======

>>>>>>> 376b5d959a0253ff28f13ace391592d990a890b1
def compare_board(b1: "Board", b2: "Board"):
    if b1.get_weight() == b2.get_weight():
        return 0
    
    return 1 if b1.get_weight() > b2.get_weight() else -1
