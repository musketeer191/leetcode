from string import ascii_lowercase

n_lower = len(ascii_lowercase)


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # a char in s is unique when it cannot be found anywhere except its current position, ie. not occur in front or behind
        # naive sol: loop thru s and check for uniqueness until found the first one, need to check the substring in front and behind,
        # opt1: speed up checking the in-front substr  by keep track of which chars already occur, so do not need to check the whole front substr
        # opt2: opt checking behind substr, as the string contains only lowercase English letters, if at some point we found out that all lowercase chars already occured but not stop yet this means all lowercases are dups, there will be no uniq, we donot need to check any more

        occured = []
        for i, ch in enumerate(s):
            if ch not in occured:
                if len(occured) == n_lower:  # all lowercases are dups
                    return -1
                if ch not in s[i + 1:]:
                    return i
                # else, ch occurs later, but it occurs the first time here, so need to record that
                occured.append(ch)

        return -1
