from config import WHITE_SPACE


class GetIndexInFinalBoardException(Exception):
    pass


class Heuristic:

    def __init__(self, matrix_final_board) -> None:
        self.__cache_position_matrix_final_board = {}
        
        for board_row, ROW in enumerate(matrix_final_board):
            for board_col, cell in enumerate(ROW):
                self.__cache_position_matrix_final_board[cell] = board_row, board_col


    def __get_index_in_final_board(self, cell: int):
        position = self.__cache_position_matrix_final_board.get(cell, None)
        if position is None:
            raise GetIndexInFinalBoardException("Não foi possível obter o índice do board final.")

        return position



    def manhattan(self, board_matrix):
        value = 0

        for board_row, ROW in enumerate(board_matrix):
            for board_col, cell in enumerate(ROW):
                if cell == WHITE_SPACE:
                    continue

                final_board_row, final_board_col = self.__get_index_in_final_board(cell)
                value += abs(board_row - final_board_row) + abs(board_col - final_board_col)

        return value



    def out_of_place(self, board_matrix):
        value = 0

        for board_row, ROW in enumerate(board_matrix):
            for board_col, cell in enumerate(ROW):
                if cell == WHITE_SPACE:
                    continue

                final_board_row, final_board_col = self.__get_index_in_final_board(cell)
                d = abs(board_row - final_board_row) + abs(board_col - final_board_col)
                value += 0 if d == 0 else 1

        return value




