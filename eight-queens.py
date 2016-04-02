import random


class Square:
    def __init__(self, column, row):
        self.col_num = column
        self.row_num = row
        self.col_str = chr(self.col_num + 64)
        self.row_str = str(self.row_num)

    def __repr__(self):
        return '{}{}'.format(self.col_str, self.row_str)

    def __str__(self):
        return '{}{}'.format(self.col_str, self.row_str)


def safe_squares(start_square, all_squares):
    """
    Returns a list of cells that a queen can't
    attack when standing on the input cell.
    :param start_square:
    :param all_squares:
    :return list:
    """
    return [cell for cell in all_squares
            if cell.row_num != start_square.row_num and  # same row
            cell.col_num != start_square.col_num and  # same column
            cell.col_num - cell.row_num != start_square.col_num - start_square.row_num and  # positive slope diagonal
            cell.col_num + cell.row_num != start_square.col_num + start_square.row_num  # negative slope diagonal
            ]


def solve(n, queen_positions=None, squares=None):
    if queen_positions is None:
        queen_positions = []
        rows = range(1, n + 1)
        columns = range(1, n + 1)
        squares = [Square(column, row) for column in columns for row in rows]
    if len(queen_positions) < n:
        if len(squares) == 0:
            return False
        result = False
        dead_squares = []
        while result is False:
            try:
                queen = [square for square in squares if square not in dead_squares][0]
            except IndexError:
                return False
            queen_positions.append(queen)
            new_squares = safe_squares(queen, squares)
            result = solve(n, queen_positions=queen_positions, squares=new_squares)
            if result is False:
                dead_squares.append(queen)
        return result
    else:
        return queen_positions


print(solve(8))
