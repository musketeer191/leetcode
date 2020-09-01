class Solution:

    def make_max_time_from_remain_digits(self, A):
        # no constraint for 2nd digit, so it should be the largest possible value, as long as it did not take away all valid values for 3rd digit
        _2nd_digit = max(A)
        print('2nd digit:', _2nd_digit)
        A.pop(A.index(_2nd_digit))

        # as mins < 60, 3rd digit must be < 6
        try:
            _3rd_digit = max([x for x in A if x < 6])
            print('3rd digit:', _3rd_digit)
            A.pop(A.index(_3rd_digit))
            _4th_digit = A[0]
            print('4th digit:', _4th_digit)
            return str(_2nd_digit) + ':' + str(_3rd_digit) + str(_4th_digit)
        except ValueError:
            return ''

    def largestTimeFromDigits(self, A) -> str:
        # the first digit in result should be the largest possible, as long as the time does not exceed 24:00,

        # hours < 24, mins < 60; so first digit must be <= 2 and 3rd digit must be < 6

        _1st_digit_pos = [x for x in A if x <= 2]
        if not _1st_digit_pos:
            return ''
        first_digit = max(_1st_digit_pos)
        print('first_digit:', first_digit)

        if first_digit < 2:
            remains = [] + A
            remains.pop(remains.index(first_digit))
            max_from_remains = self.make_max_time_from_remain_digits(remains)
            if max_from_remains != '':
                return str(first_digit) + max_from_remains
            return ''

        # 1st digit is 2, then a valid time must have its 2nd digit < 4. If no such valid time exist, need to fall back to case when 1st digit < 2.
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
                return str(first_digit) + str(_2nd_digit) + ':' + str(_3rd_digit) + str(_4th_digit)
            except ValueError:
                print('cannot find any valid value for 3rd digit')
                try:    # cases when first digit < 2
                    first_digit = max([x for x in A if x < 2])
                    max_from_remains = self.make_max_time_from_remain_digits(A)
                    if max_from_remains != '':
                        return str(first_digit) + max_from_remains
                    return ''
                except ValueError:
                    return ''
        except ValueError:
            try:    # cases when first digit < 2
                first_digit = max([x for x in A if x < 2])
                max_from_remains = self.make_max_time_from_remain_digits(A)
                if max_from_remains != '':
                    return str(first_digit) + max_from_remains
                return ''
            except ValueError:
                return ''

if __name__ == '__main__':
    sol = Solution()
    sol.largestTimeFromDigits([0,2,6,6])