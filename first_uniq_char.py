
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count occurence of each char, a uniq char has count == 1
        # this should be fast as it has only 1 pass thru s.
        # NOTE: instead of re-invent the counter, using the built-in counter in collections module
        # will be faster as the latter use a hash map, so will speed up lookup ops

        occur = dict()
        for i, ch in enumerate(s):
            try:
                occur[ch] += 1
            except KeyError:
                occur[ch] = 1

        for i, ch in enumerate(s):
            if occur[ch] == 1:
                return i
        return -1
