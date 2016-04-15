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


def slope(y2, y1, x2, x1):
    return (y2 - y1) / (x2 - x1)


def safe_squares(queen_pos, all_squares):
    """
    Returns a list of cells that a queen can't
    attack when standing on the input cell.
    :param start_square:
    :param all_squares:
    :return list:
    """
    return [cell for cell in all_squares
            if cell.row_num != queen_pos.row_num and  # same row
            cell.col_num != queen_pos.col_num and  # same column
            slope(queen_pos.row_num, cell.row_num, queen_pos.col_num, cell.col_num) not in [1, -1]  # Diagonals
            ]


def solve(num_queens, rows, columns, queen_positions=None, squares=None, depth=0):
    """
    Recursive function
    Depth first search
    with backtracking
    """
    if queen_positions is None:
        queen_positions = []
        squares = [Square(column, row) for column in range(1, columns+1) for row in range(1, rows+1)]

    if len(queen_positions) < num_queens:
        if len(squares) == 0:
            return False
        result = False
        dead_squares = []
        while result is False:
            safe_squares_minus_dead_squares = [square for square in squares if square not in dead_squares]
            if len(safe_squares_minus_dead_squares) > 0:
                new_queen = safe_squares_minus_dead_squares[0]
            else:
                return False
            queen_positions.append(new_queen)
            new_squares = safe_squares(new_queen, squares)
            result = solve(num_queens, rows, columns, queen_positions, new_squares, depth+1)
            if result is False:
                dead_squares.append(new_queen)
                queen_positions.pop()
        return result
    else:
        return queen_positions


def main(n):
    result = solve(n, n, n)
    if result is False:
        print('2x2 and 3x3 boards do not have solutions')
    else:
        print(result)

main(3)
