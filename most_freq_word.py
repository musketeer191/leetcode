import re
import collections
from string import punctuation
from bisect import bisect_left


class Solution:
    def is_in_banned(self, w, banned):
        # given a word and a sorted list of banned words, return if the word is in banned words
        idx = bisect_left(banned, w)
        if (idx < len(banned)) and (banned[idx] == w):
            return True
        return False

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # need to count occurence of words not in banned list
        # as we not care about punctuation, should strip them away
        # not case sensitive, so just convert all to lower cases
        # simple sol: split the paragraph into words,
        # loop thru the list to count occurence of words:
        # if meet a word not in banned, increment its count

        # complexity: for each word need to search for it in banned list, so log(len(banned)) if banned is sorted, then look up its count to increase, which is O(1) if the counts are stored in a hashmap. So final complexity is len(words) * log(len(banned))

        # lower case
        s = paragraph.lower()
        # strip punctuations & split into words
        # note edge case: the string has words delimited by comma, or some punctuation
        regex = re.compile('[%s]' % re.escape(punctuation))
        words = regex.sub(' ', s).split()

        banned = sorted(banned)
        count = collections.Counter()
        for w in words:
            if not self.is_in_banned(w, banned):
                count[w] += 1

        return count.most_common(1)[0][0]

