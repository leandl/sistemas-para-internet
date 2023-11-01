from entities.board import Board
from a_star_algorithm import AStarAlgorithm
<<<<<<< HEAD
from utils import generate_initial_board, generate_final_board, compare_board
from heuristic import Heuristic

MATRIX_FINAL_BOARD = generate_final_board()

heuristic = Heuristic(MATRIX_FINAL_BOARD)
# h = lambda _board: 0
# h = heuristic.out_of_place
h = heuristic.manhattan

FINAL_BOARD = Board(MATRIX_FINAL_BOARD, h)
initial_board = generate_initial_board(FINAL_BOARD, MOVEMENTS=100)
initial_board = Board([
    ["_", 3, 5],
    [1, 2, 7],
    [6, 4,8]
], h)
=======
from utils import generate_initial_board,  generate_final_board, compare_board
from heuristic import Heuristic

MATRIX_FINAL_BOARD = generate_final_board()
# MATRIX_FINAL_BOARD = [
#     ["A", "B", "C"],
#     ["D", "E", "F"],
#     ["G", "H", "_"]
# ]

heuristic = Heuristic(MATRIX_FINAL_BOARD)

h = lambda _board: 0
h = heuristic.out_of_place
h = heuristic.greater_distance
h = heuristic.manhattan


FINAL_BOARD = Board(MATRIX_FINAL_BOARD, h)
initial_board = generate_initial_board(FINAL_BOARD, MOVEMENTS=20)
# initial_board = Board([['_', 3, 8], [4, 6, 5], [1, 7, 2]], h)

>>>>>>> 376b5d959a0253ff28f13ace391592d990a890b1

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
    path, visited, pending, movements = result
        
    for p in path:
        print_matrix(p.get_matrix())

    print(f"Visitados: {visited}")
    print(f"Pendentes: {pending}")
    print(f"Visitados e Pendentes: {pending + visited}")
    print(f"Moves: {movements}")
