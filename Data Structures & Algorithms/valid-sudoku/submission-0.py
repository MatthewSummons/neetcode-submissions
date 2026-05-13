class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row Check
        for row in board:
            check_set = set()
            for symbol in row:
                if symbol == ".": continue
                if symbol in check_set: return False
                else: check_set.add(symbol)
        # Column Check
        for col_num in range(9):
            check_set = set()
            for row in board:
                symbol = row[col_num]
                if symbol == ".": continue
                if symbol in check_set: return False
                else: check_set.add(symbol)
        # 3x3 Grid
        for box_x in range(3):
            for box_y in range(3):
                grid_set = set()
                for row_offset in range(3):
                    grid_row = board[3 * box_x + row_offset][3 * box_y: 3 * box_y + 3]
                    for symbol in grid_row:
                        if symbol == ".": continue
                        if symbol in grid_set: return False
                        else: grid_set.add(symbol)
        return True
        