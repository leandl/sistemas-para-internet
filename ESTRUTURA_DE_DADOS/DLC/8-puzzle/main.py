from entities.board import Board
from utils import generate_final_board, generate_initial_board, manhattan

MATRIX_FINAL_BOARD = generate_final_board()
FINAL_BOARD = Board(MATRIX_FINAL_BOARD, manhattan)
initial_board = generate_initial_board(FINAL_BOARD, MOVES=5)

# print(initial_board.get_matrix())
# print(FINAL_BOARD.get_matrix())


def print_matrix(m):
    print("-=-=-=-=-=-=-")
    for row in m:
        print(row)
    print("-=-=-=-=-=-=-")

board_passed = []

# print(FINAL_BOARD in [copy.deepcopy(FINAL_BOARD)])
        
current_board = initial_board
print_matrix(current_board.get_matrix())
board_passed.append(initial_board)
while not current_board.get_weight() == 0:
    boards = current_board.next_boards()
    boards = [x for x in boards if x not in board_passed]
    lower_board = None
    for board in boards:
        if lower_board is None:
            lower_board = board
            continue

        lower_board = board if board.get_weight() < lower_board.get_weight() else lower_board

    print_matrix(lower_board.get_matrix())
    current_board = lower_board
    board_passed.append(lower_board)  


# # # for x in list_boards:
# # #     print(x)



# # # print(manhattan(board))

# # print(generate_options(board))