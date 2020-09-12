class Solution:
    from functools import reduce
    def product(self, nums):
        return reduce(lambda x, y: x * y, nums)

    def find_first_neg(self, nums):
        # given a list of numbers with at least 1 neg, return the first neg
        for i in range(len(nums)):
            if nums[i] < 0:
                return i

    def find_last_neg(self, nums):
        # given a list of numbers with at least 1 neg, return the last neg
        return len(nums) - 1 - self.find_first_neg(nums[::-1])

    def maxProduct(self, nums: List[int]) -> int:
        # if nums[i]=0, then the products of subarrays containing nums[i] will be 0, so results will be max(maxProduct(nums[:i]), maxProduct(nums[i+1:]), 0)
        # repeat this process let us reach subarrays with no 0, so the products will be non-zero
        # for such an array a[1:k] of integers,
        # if a[1]...a[k] > 0: it will be the max product, because
        # a[1]...a[k] = abs(a[1]...a[k]) >= abs(a[i]...a[j]) >= a[i]...a[j]
        # more general if
        # else, a[1]...a[k] < 0, then there must be an odd numbers of neg factors, say 2m+1, if the first neg number occurs at index i_f and the last neg numbers occur at i_l then the two longest (thus largest) pos products are prod(a[:i_l]) and prod(a[i_f + 1:]) as each contains 2m neg factors
        # print('nums:', nums)
        if not nums:
            return float('-inf')
        # else
        if 0 in nums:
            i = nums.index(0)
            return max(0, self.maxProduct(nums[:i]), self.maxProduct(nums[i + 1:]))
        # else
        prod = self.product(nums)
        if prod > 0:
            return prod
        # else, prod < 0
        first_neg = self.find_first_neg(nums)
        last_neg = self.find_last_neg(nums)
        last_idx = len(nums) - 1
        if (last_neg > 0) and (first_neg + 1 <= last_idx):
            return max(self.product(nums[:last_neg]), self.product(nums[first_neg + 1:]))
        if last_neg == 0:
            if len(nums) > 1:
                return self.product(nums[1:])
            return nums[0]
        if first_neg == last_idx:
            return self.product(nums[:first_neg])

