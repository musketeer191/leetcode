class Solution:

    def find_max_time_with_1st_digit_less_than2(self, A):
        try:
            first_digit = max([x for x in A if x < 2])
            remains = [] + A
            remains.pop(remains.index(first_digit))
            # no constraint for 2nd digit, so it should be the largest possible value, as long as it did not take away all valid values for 3rd digit
            _2nd_digit = max(remains)
            # print('2nd digit:', _2nd_digit)
            remains.pop(remains.index(_2nd_digit))
            # as mins < 60, 3rd digit must be < 6
            try:
                _3rd_digit = max([x1 for x1 in remains if x1 < 6])
                # print('3rd digit:', _3rd_digit)
                remains.pop(remains.index(_3rd_digit))
                _4th_digit = remains[0]
                # print('4th digit:', _4th_digit)
                return str(first_digit) + str(_2nd_digit) + ':' + str(_3rd_digit) + str(_4th_digit)
            except ValueError:
                return ''
        except ValueError:
            return ''

    def largestTimeFromDigits(self, A) -> str:
        # the first digit in result should be the largest possible, as long as the time does not exceed 24:00,

        # hours < 24, mins < 60; so first digit must be <= 2 and 3rd digit must be < 6

        if 2 not in A:
            try:
                return self.find_max_time_with_1st_digit_less_than2(A)
            except ValueError:
                return ''

        print('Find max time among cases with first digit < 2')
        max1 = self.find_max_time_with_1st_digit_less_than2(A)

        print('If there are valid cases with first digit = 2, Find Max time among them')
        first_digit = 2
        A.pop(A.index(first_digit))
        # A valid time must have its 2nd digit < 4 and 3rd digit < 6.
        # If no such valid time exist, fall back to case when 1st digit < 2.
        try:
            _2nd_digit = max([x for x in A if x < 4])
            print('2nd digit:', _2nd_digit)
            A.pop(A.index(_2nd_digit))
            try:
                _3rd_digit = max([x for x in A if x < 6])
                print('3rd digit:', _3rd_digit)
                A.pop(A.index(_3rd_digit))
                _4th_digit = A[0]
                print('4th digit:', _4th_digit)
                max2 = str(first_digit) + str(_2nd_digit) + ':' + str(_3rd_digit) + str(_4th_digit)
                return max2
            except ValueError:
                print('\tno valid cases as no valid value for 3rd digit')
                print('so the max time possible is: ', max1)
                return max1
        except ValueError:
            print('\tno valid cases as no valid value for 2nd digit')
            print('so the max time possible is: ', max1)
            return max1


if __name__ == '__main__':
    sol = Solution()
    sol.largestTimeFromDigits([0, 2, 6, 6])
