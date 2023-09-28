import copy
from typing import List
from config import WHITE_SPACE, BOARD_ROW, BOARD_COL

BOARD_DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

class Board:

    def __init__(self, matrix, heuristic):
        self.__matrix = matrix
        self.__weight = heuristic(matrix)
        self.__heuristic = heuristic

    def get_matrix(self):
        return self.__matrix

    def get_weight(self):
        return self.__weight

    def __eq__(self, board: "Board"):
        if not isinstance(board, Board):
            return False

        return self.get_matrix() == board.get_matrix()


    def __iter__(self):
        board = self.__matrix
        for board_row, ROW in enumerate(board):
            for board_col, cell in enumerate(ROW):
                yield board_row, board_col, cell

    def next_boards(self) -> List["Board"]:
        position_row = None
        position_col = None

        for board_row, board_col, cell in self:
            if cell == WHITE_SPACE:
                position_row = board_row
                position_col = board_col

                break

        next_boards = []
        for row, col in BOARD_DIRECTIONS:
            new_position_row = position_row + row
            new_position_col = position_col + col

            if (new_position_row >= BOARD_ROW or new_position_row < 0):
                continue

            if (new_position_col >= BOARD_COL or new_position_col < 0):
                continue

            new_board_matrix = copy.deepcopy(self.__matrix)

            tmp = new_board_matrix[position_row][position_col]
            new_board_matrix[position_row][position_col] = new_board_matrix[new_position_row][new_position_col]
            new_board_matrix[new_position_row][new_position_col] = tmp

            new_board = Board(new_board_matrix, self.__heuristic)
            next_boards.append(new_board)

        return next_boards
    
    def __str__(self) -> str:
        return self.__matrix.__str__()