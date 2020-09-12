DIGITS = [i + 1 for i in range(9)]


class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # to avoid duplicated sols, we will force that the next entry in a sol must be larger than current entry
        # recursive: try each v of possible values, then the remaining k-1 values must sum up to n-v and they must be chosen from values larger than v
        return self.find_combi(k, n, DIGITS)

    def find_combi(self, k: int, n: int, ls: List[int]) -> List[List[int]]:
        # given a sorted list of positive integers, return combinations of k unique values in the list which sum up to n
        # print('k:', k)
        # print('n:', n)
        # print('values in list:', ls)

        # stop cond
        if k == 0 and n == 0:  # found a combi
            return [[]]
        if k == 0 and n != 0:  # fail
            return []

        # min and max sums of k unique values in the list
        min_sum, max_sum = sum(ls[:k]), sum(ls[-k:])
        # print('sums of', k, 'unique values in the list must be from', min_sum, 'to', max_sum)
        if (n < min_sum) or (n > max_sum):
            return []
        # else, try possibilities backward
        sols = []
        for i in range(len(ls) - k + 1):
            v = ls[i]
            # print('try value:', v)
            sols_start_with_v = [[v] + c for c in self.find_combi(k - 1, n - v, ls[i + 1:])]
            sols += sols_start_with_v
        return sols
