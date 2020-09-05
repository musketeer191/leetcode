# clarify: parts are contiguous?
# import collections


class Solution:
    def find_last_occur(self, ch, S):
        # last occur is the first occur in reverse order
        try:
            return len(S) - 1 - S[::-1].index(ch)
        except ValueError:
            return -1

    def find_distinct_chars(self, s):
        count = collections.Counter(s)
        return count.keys()

    def extend_till_cover_all_occurence(self, part, S):
        # print('init part:', part)

        q = collections.deque(self.find_distinct_chars(part))
        # print('init queue:', q)
        end = len(part)

        while q:
            # each time, process the whole group in queue by finding the furthest extension possible
            last_occurs = [self.find_last_occur(ch, S) for ch in q]
            idx = max(last_occurs) + 1  # furthest extension possible
            if idx > end:
                to_add = S[end: idx]
                part += to_add
                # print('\t updated part:', part)
                # update end of part
                end = idx
                # update queue: empty old group and add new group from to_add (if any)
                q.clear()
                for ch in to_add:
                    if ch not in q:
                        q.append(ch)
                # print('\t updated queue:', q)
            else:
                q.clear()
        return part

    def partitionLabels(self, S: str) -> List[int]:
        # partition into as many as parts possible s.t. parts have no common letters
        # return lists of sizes of the parts

        # the split with max number of parts is splitting S into individual chars, but then parts can have common letters, when some letter is repeated
        # if a char occurs many times, then all its occurence must be in the same partition, so the partition need to cover the range from its first to last occurence
        # a unique letter can be a partition itself and this part surely has no common letter with others
        # Simple sol: count occurence of letters to find unique and repeated letters, if s0 is uniq, then it is a partition and just need to partition remaining chars (recursive). Else, then find last occur of s0, say at i, then the range from 0 to i (inclusive) contains all occurence of s0, so the first partition need to cover at least "occur range". For each char uniq in that range, find its last occurence and extend furthest possible. This will give us the first partition, then repeat.

        # stop
        if not S:
            return []

        i = self.find_last_occur(S[0], S)
        if i == 0:  # s0 is unique
            return [1] + self.partitionLabels(S[1:])
        # else, s0 not unique
        part0 = S[:(i + 1)]

        # extend part0 until it covers occur ranges of all its letters
        part0 = self.extend_till_cover_all_occurence(part0, S)

        return [len(part0)] + self.partitionLabels(S[len(part0):])
