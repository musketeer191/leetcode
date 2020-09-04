class Solution:
    def found_pair_not_far(self, sorted_a, t):
        # only need to check consecutive pairs
        last = len(sorted_a) - 1
        for i in range(last):
            if abs(sorted_a[i + 1] - sorted_a[i]) <= t:
                print('found a pair with dist at most', t)
                print([sorted_a[i], sorted_a[i + 1]])
                return True
        return False

    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        # is there a pair i, j s.t. :
        # dist between nums[i] and nums[j] is <= t and the dist between i and j is <= k

        # brute-force: loop thru all pairs i < j s.t. 0 < j-i <= k until finding a pair s.t. abs(nj - ni) <= t
        # j-i=1: (0,1),...(n-2,n-1) -> n-1 pairs
        # j-i=d: (0,d),...,(n-1-d, n-1), -> n-d pairs
        # number of pairs is O(n^2)

        # if the array is already sorted then dist(n[i], n[i+1]) <= dist(n[i], n[i+d]) for all d>=1, thus if there exist dist(n[i], n[i+d]) <= t then dist(n[i], n[i+1]) <= t. flip side, if dist(n[i], n[i+1]) <= t then pair i, i+1 satisfying.

        # use sliding windows of size k
        # first window of size k: n0,..., n[k], find if there is any pair -> can sort this window
        # 2nd window of size k: n[1], ..., n[k], n[k+1], the pairs in range n[1:k] already checked, so only need to check new pairs (n[k+1], n[i]) for i=1:k -> k such pairs
        # repeat until exhaust all windows

        w0 = nums[:(k + 1)]
        print('first window:', w0)
        if self.found_pair_not_far(sorted(w0), t):
            return True

        m = len(nums)
        # check i-th window, given that (i-1)-th window already checked
        for i in range(1, m - k):
            # i-th window n[i:i+k+1]
            start, end = i, i + k + 1
            w_i = nums[start:end]
            print(i+1, '-th window:', w_i)
            last = w_i[-1]
            # check k new pairs (last, w_i[j])
            for j in range(k):
                if abs(last - w_i[j]) <= t:
                    print('found a pair with dist at most', t)
                    print([last, w_i[j]])
                    return True
        return False


if __name__ == '__main__':
    nums = [3, 6, 0, 4]
    k = 2
    t = 2
    print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
