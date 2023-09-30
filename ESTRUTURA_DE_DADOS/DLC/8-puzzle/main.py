from entities.board import Board
from a_star_algorithm import AStarAlgorithm
from utils import generate_initial_board, MATRIX_FINAL_BOARD
from heuristic import heuristic

h = lambda _board: 0
h = heuristic["out_of_place"]
h = heuristic["manhattan"]

FINAL_BOARD = Board(MATRIX_FINAL_BOARD, h)
initial_board = generate_initial_board(FINAL_BOARD, MOVEMENTS=20)
# initial_board = Board(
#     heuristic=h,
#     matrix=[
#         [2, 6, 4],
#         [1, "_", 8],
#         [7, 3, 5]
#     ]
# )



def compare_board(b1: "Board", b2: "Board"):
    if b1.get_weight() == b2.get_weight():
        return 0
    
    return 1 if b1.get_weight() > b2.get_weight() else -1


def print_matrix(m):
    print("-=-=-=-")

    for row in m:
        print(" " + " ".join([str(col) for col in row]))
    print("-=-=-=-")

print("Board Inicial")
print_matrix(initial_board.get_matrix())
print("")
print("Board Final")
print_matrix(FINAL_BOARD.get_matrix())

print("")

result = AStarAlgorithm.execute(initial_board, FINAL_BOARD, compare_board)
if result is None:
    print("Não foi possivel resolver")
else:
    path, visited, movements = result
        
    for p in path:
        print_matrix(p.get_matrix())

    print(f"Visitados: {visited}")
    print(f"Moves: {movements}")
