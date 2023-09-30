from config import WHITE_SPACE
from utils import get_index_in_final_board

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
