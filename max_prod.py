class Solution:
    def find_last_zero(self, ls):
        try:
            return len(ls) - 1 - ls[::-1].index(0)
        except ValueError:
            return -1

    def maxProduct(self, nums: List[int]) -> int:
        # sol:
        # suppose that we already know the max product mp from subarrays up to index k-1, now we add item a[k]. This will create new products a[k]...a[i], which may be larger than mp. So we need to compare the new products with each other and with mp to get the new max. Repeat the process until finish.
        # complexity: for each k, need to do k+1 multiplications => sum_k(k+1) = O(n^2)
        # mp = -float('inf')
        # for k in range(len(nums)):
        #     p = 1
        #     for i in range(k, -1, -1):
        #         p *= nums[i]
        #         if p > mp:
        #             mp = p
        # return mp

        # opt sol:
        # Remark: if a[1]...a[k] > 0 then a[1]...a[k] is the max of new products, and we only need to compare its against current max.
        # if a[1]...a[k] > 0 then:
        # all a[i] != 0; thus abs(a[j]) >= 1
        # a[1]...a[k] = abs(a[1]...a[k]) >= abs(a[i]...a[k]) >= a[i]...a[k], for all i in [1,k].

        # the var to keep track of products a[1]...a[k]
        prod = 1
        mp = -float('inf')
        for k in range(len(nums)):
            prod *= nums[k]
            if nums[k] == 0:
                if mp < 0:
                    mp = 0
            else:  # nums[k] != 0
                if prod > 0:
                    if prod > mp:
                        mp = prod
                elif prod == 0:
                    # a zero factor will make whole product zero
                    # going backward from a[k], find the first zero
                    for j in range(k, -1, -1):
                        if nums[j] == 0:
                            break
                            # a[i]...a[k]=0, for all i <= j, only to compute a[i]...a[k] for i >j
                    p = 1
                    for i in range(k, j, -1):
                        p *= nums[i]
                        if p > mp:
                            mp = p
                    if 0 > mp:
                        mp = 0
                else:
                    p = 1
                    for i in range(k, -1, -1):
                        p *= nums[i]
                        if p > mp:
                            mp = p
        return mp
