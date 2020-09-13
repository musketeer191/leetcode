class Solution:

    def __init__(self):
        self.queen_cells = []
        self.atk_region = []
        return

    def get_hill_diag(self, row, col, n):
        return [(row + d, col + d) for d in range(max([-row, -col]), n + min([-row, -col])) if d != 0]

    def get_dale_diag(self, row, col, n):
        max_row = max_col = (n - 1)
        start = max([-col, row - max_row])
        end = min([row, max_col - col]) + 1
        return [(row - d, col + d) for d in range(start, end) if d != 0]

    def is_not_under_attack(self, row, col):
        # check if the cell (row, col) is under atk by any previous queen
        # this search seem expensive
        # TODO: opt by
        return (row, col) not in self.atk_region

    def place_queen(self, row, col):
        # print('placed a queen at the cell', (row, col))
        self.queen_cells.append((row, col))

    def find_cells_under_atk_by_queen(self, row, col, n):
        row_atk = [(row, c) for c in range(n) if c != col]
        col_atk = [(r, col) for r in range(n) if r != row]
        # hill diag passing (row, col)
        hill_atk = self.get_hill_diag(row, col, n)
        # dale diag passing (row, col)
        dale_atk = self.get_dale_diag(row, col, n)
        cells_under_atk_by_queen = row_atk + col_atk + hill_atk + dale_atk
        # print('\t cells_under_atk_by_queen at', (row, col), ':', cells_under_atk_by_queen)
        return cells_under_atk_by_queen

    def remove_queen(self, row, col):
        # print('removed a queen from the cell', (row, col))
        self.queen_cells.remove((row, col))

    # template
    def backtrack_nqueen(self, n, row=0, count=0):
        for col in range(n):
            # iterate through columns at the curent row.
            if self.is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                self.place_queen(row, col)
                new_cells_under_atk = self.find_cells_under_atk_by_queen(row, col, n)
                self.atk_region += new_cells_under_atk
                # print('\t Region under atk after placing the queen:', self.atk_region)
                if row + 1 == n:
                    # we reach the bottom, i.e. we find a solution!
                    count += 1
                    print('A solution:', self.queen_cells)
                else:
                    # we move on to the next row
                    count = self.backtrack_nqueen(n, row + 1, count)
                # backtrack, i.e. remove the queen and remove the attacking zone.
                self.remove_queen(row, col)
                n_remain = len(self.atk_region) - len(new_cells_under_atk)
                self.atk_region = self.atk_region[:n_remain]
                # print('\t Region under atk after removing the queen:', self.atk_region)
        return count

    def totalNQueens(self, n: int) -> int:
        # call actual workhorse here
        return self.backtrack_nqueen(n, row=0, count=0)
