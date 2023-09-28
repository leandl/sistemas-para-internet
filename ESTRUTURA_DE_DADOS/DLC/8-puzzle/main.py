from entities.board import Board
from entities.ordered_vertor import OrderedVector
from utils import generate_final_board, generate_initial_board, heuristic

# h = heuristic["out_of_place"]
h = heuristic["manhattan"]

MATRIX_FINAL_BOARD = generate_final_board()
FINAL_BOARD = Board(MATRIX_FINAL_BOARD, h)
initial_board = generate_initial_board(FINAL_BOARD, MOVES=7)

print(initial_board.get_matrix())
print(FINAL_BOARD.get_matrix())

def compare_board(b1: "Board", b2: "Board"):
    if b1.get_weight() == b2.get_weight():
        return 0
    
    return 1 if b1.get_weight() > b2.get_weight() else -1


def print_matrix(m):
    print("-=-=-=-")

    for row in m:
        print(" " + " ".join([str(col) for col in row]))
    print("-=-=-=-")

board_passed = [initial_board]    
parents = {}
orderedBoards = OrderedVector(10_000, compare_board)
orderedBoards.insert(initial_board)
current_board = None

while not len(orderedBoards) == 0:
    current_board = orderedBoards.pop(0)
    if current_board == FINAL_BOARD:
        break

    boards = current_board.next_boards()
    boards = [x for x in boards if x not in board_passed]
    for board in boards:
        board_passed.append(board)
        parents[str(board)] = current_board
        orderedBoards.insert(board)
   
if not current_board == FINAL_BOARD:
    print("Não foi possivel resolver")
else:
    path = [current_board]
    while not parents.get(str(current_board), None) == None:
        parent = parents[str(current_board)]
        path.insert(0, parent)
        current_board = parent
        
    # for p in path:
    #     print_matrix(p.get_matrix())

    print("Visitados: " + str(len(board_passed)))
    print("Moves: " + str(len(path) -1) )
# # # for x in list_boards:
# # #     print(x)



# # # print(manhattan(board))

# print(generate_options(board))