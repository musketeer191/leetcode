# when multiply two sparse vectors a and b, remaining terms are from indices i where both a[i] and b[i] are non-zeros
# so we only need to keep track of non-zeroes of a sparse vector, which also leads to an efficient storage of a sparse vector

class SparseVector:
    def __init__(self, n_entry: int, non_zeroes: dict):
        # if nonzero_idx[-1] >= n_entry:
        #     print('index out of bound error')
        #     return

        self.n_entry = n_entry
        self.non_zeroes = non_zeroes

    def get_value(self, i: int):
        # given index of a non-zero value in a sparse vector, return the value at the index
        try:
            return self.non_zeroes[i]
        except KeyError:
            return 0


def mul_sparse(a: SparseVector, b: SparseVector) -> int:
    if a.n_entry != b.n_entry:
        print('dim mismatch, cannot multiply!')
        return
    if (not a.nonzero_idx) or (not b.nonzero_idx):
        return 0
    return sum([a.get_value(i) * b.get_value(i) for i in set(a.nonzero_idx) & set(b.nonzero_idx)])


def to_sparse(v: List[int]) -> SparseVector:
    # print('vector:', v)
    n_entry = len(v)
    non_zeroes = get_non_zeroes(v)
    sv = SparseVector(n_entry, non_zeroes)
    # print('its sparse form:', (sv.n_entry, sv.nonzero_idx, sv.values))
    return sv


def get_non_zeroes(a):
    non_zeroes = {}
    for i, v in enumerate(a):
        if v != 0:
            non_zeroes[i] = v
    return non_zeroes


# This part is for space opt
# Compressed Sparse Column/Row Matrix: for a sparse matrix, only need to store non-zero cols
# also, columns of a matrix share the same number of rows
class CSC_Matrix:
    def __init__(self, A):
        self.n_row = len(A)
        self.n_col = len(A[0])
        self.non_zero_cols = {}
        for c in range(self.n_col):
            a_c = [A[r][c] for r in range(self.n_row)]
            if any([a_c != 0]):
                self.non_zero_cols[c] = get_non_zeroes(a_c)

    def get_col(self, c):
        try:
            return SparseVector(n_entry=self.n_row, non_zeroes=self.non_zero_cols[c])
        except KeyError:
            return SparseVector(n_entry=self.n_row, non_zeroes={})
        pass


class CSR_Matrix:
    def __init__(self, A):
        self.n_row = len(A)
        self.n_col = len(A[0])
        self.non_zero_rows = {}  # map each row to its non-zeroes
        for r in range(self.n_row):
            if any(A[r] != 0):
                self.non_zero_row_idx.append(r)
                self.non_zero_rows[r] = get_non_zeroes(A[r])

    def get_row(self, r):
        try:
            return SparseVector(n_entry=self.n_col, non_zeroes=self.non_zero_rows[r])
        except KeyError:
            return SparseVector(n_entry=self.n_col, non_zeroes={})


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # let res be the result matrix, then res[i][j] = A[i][:] * B[:][j]
        # for each row A[r][:], create a sparse vector from it, then for each column  B[:][c], create a sparse vector, then multiply them together

        n_row_in_a = len(A)
        res = []
        csc_b = CSC_Matrix(B)
        for r in range(n_row_in_a):
            a_r = to_sparse(A[r][:])
            res.append([mul_sparse(a_r, csc_b.get_col(c)) for c in range(csc_b.n_col)])
        return res
        # n_row_in_a = len(A)
        # n_row_in_b = len(B)
        # n_col_in_b = len(B[0])
        # b_sparse = [to_sparse([B[r][c] for r in range(len(B))]) for c in range(n_col_in_b)]
        # for r in range(n_row_in_a):
        #     a_r = to_sparse(A[r][:])
        #     res.append([mul_sparse(a_r, b_sparse[c]) for c in range(n_col_in_b)])
        # return res
