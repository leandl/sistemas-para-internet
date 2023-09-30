from entities.ordered_vertor import OrderedVector


class AStarAlgorithm:
    
    @staticmethod
    def execute(initial_board, final_board, compare):
        board_passed = [initial_board]    
        parents = {}
        ordered_boards = OrderedVector(10_000, compare)
        ordered_boards.insert(initial_board)
        current_board = None

        while len(ordered_boards) > 0:
            current_board = ordered_boards.pop(0)
            if current_board == final_board:
                break

            boards = current_board.next_boards()
            boards = [x for x in boards if x not in board_passed]
            for board in boards:
                board_passed.append(board)
                parents[str(board)] = current_board
                ordered_boards.insert(board)
        
        if current_board != final_board:
            return None
        
        path = [current_board]
        while parents.get(str(current_board), None) != None:
            parent = parents[str(current_board)]
            path.insert(0, parent)
            current_board = parent


        visited = len(board_passed)
        movements = len(path) -1
        return path, visited, movements
