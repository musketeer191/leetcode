from itertools import chain


def get_hill_diag(row, col, n):
    return [(row + d, col + d) for d in range(max([-row, -col]), n + min([-row, -col]))]


def get_dale_diag(row, col, n):
    max_row = max_col = (n - 1)
    start = max([-col, row - max_row])
    end = min([row, max_col - col]) + 1
    return [(row - d, col + d) for d in range(start, end)]


class Solution:

    def __init__(self):
        self.queen_cells = []
        # self.atk_region = []
        return

    def init_valid_region(self, n):
        self.valid_region = set(chain.from_iterable([[(r, c) for c in range(n)] for r in range(n)]))
        return

    def is_not_under_attack(self, row, col):
        # check if the cell (row, col) is under atk by any previous queen

        # return self.queens_atk[row][col] == 0
        # this search seem expensive -> TODO: build a BST to speed it up
        return (row, col) in self.valid_region

    def place_queen(self, row, col):
        # print('\t placed a queen at the cell', (row, col))
        self.queen_cells.append((row, col))

    def remove_queen(self, row, col):
        # print('\t removed a queen from the cell', (row, col))
        self.queen_cells.remove((row, col))

    def find_cells_under_atk_by_queen(self, row, col, n):
        cell = (row, col)
        row_atk = [(row, c) for c in range(n)]
        col_atk = [(r, col) for r in range(n)]
        # hill diag passing (row, col)
        hill_atk = get_hill_diag(row, col, n)
        # dale diag passing (row, col)
        dale_atk = get_dale_diag(row, col, n)
        cells_under_atk_by_queen = set(row_atk + col_atk + hill_atk + dale_atk)
        # print('\t cells_under_atk_by_queen at', (row, col), ':', cells_under_atk_by_queen)
        return cells_under_atk_by_queen

    def backtrack_nqueen(self, n, row=0, count=0):
        for col in range(n):
            # iterate through columns at the curent row.
            if self.is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                self.place_queen(row, col)
                new_cells_under_atk = self.find_cells_under_atk_by_queen(row, col, n)
                to_drop = self.valid_region.intersection(new_cells_under_atk)
                self.valid_region = self.valid_region - to_drop
                # print('\t valid region after placing the queen:', self.valid_region)

                if row + 1 == n:
                    # we reach the bottom, i.e. we find a solution!
                    count += 1
                    # print('A solution:', self.queen_cells)
                else:
                    # we move on to the next row
                    count = self.backtrack_nqueen(n, row + 1, count)
                # backtrack, i.e. remove the queen and remove the attacking zone.
                self.remove_queen(row, col)
                self.valid_region = self.valid_region.union(to_drop)
                # print('\t valid region after removing the queen:', self.valid_region)
        return count

    def totalNQueens(self, n: int) -> int:
        self.init_valid_region(n)
        # call actual workhorse here
        return self.backtrack_nqueen(n, row=0, count=0)
