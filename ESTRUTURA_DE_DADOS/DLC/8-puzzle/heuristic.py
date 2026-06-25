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

    def manhattan_with_linear_conflict(self, board_matrix):
        return self.manhattan(board_matrix) + (
            2 * self.__count_linear_conflicts(board_matrix)
        )


    def __count_linear_conflicts(self, board_matrix):
        return (
            self.__count_row_conflicts(board_matrix)
            + self.__count_column_conflicts(board_matrix)
        )


    def __count_row_conflicts(self, board_matrix):
        conflicts = 0

        for row, ROW in enumerate(board_matrix):
            for left_col, left_tile in enumerate(ROW):

                if left_tile == WHITE_SPACE:
                    continue

                goal_row_left, goal_col_left = self.__get_index_in_final_board(left_tile)

                if goal_row_left != row:
                    continue

                for right_col in range(left_col + 1, len(ROW)):
                    right_tile = ROW[right_col]

                    if right_tile == WHITE_SPACE:
                        continue

                    goal_row_right, goal_col_right = self.__get_index_in_final_board(right_tile)

                    if goal_row_right != row:
                        continue

                    if goal_col_left > goal_col_right:
                        conflicts += 1

        return conflicts


    def __count_column_conflicts(self, board_matrix):
        conflicts = 0

        total_rows = len(board_matrix)
        total_cols = len(board_matrix[0])

        for col in range(total_cols):
            for top_row in range(total_rows):
                top_tile = board_matrix[top_row][col]

                if top_tile == WHITE_SPACE:
                    continue

                goal_row_top, goal_col_top = self.__get_index_in_final_board(top_tile)

                if goal_col_top != col:
                    continue

                for bottom_row in range(top_row + 1, total_rows):
                    bottom_tile = board_matrix[bottom_row][col]

                    if bottom_tile == WHITE_SPACE:
                        continue

                    goal_row_bottom, goal_col_bottom = self.__get_index_in_final_board(bottom_tile)

                    if goal_col_bottom != col:
                        continue

                    if goal_row_top > goal_row_bottom:
                        conflicts += 1

        return conflicts
