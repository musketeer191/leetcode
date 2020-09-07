class Solution:
    def find_occurs(self, x, ls):
        return [i for i, e in enumerate(ls) if e == x]

    def drop_items_at_indices(self, ls, indices) -> list:
        all_idx = set(range(len(ls)))
        to_drop = set(indices)
        return [ls[i] for i in all_idx - to_drop]

    def follow_pattern(self, pattern, words):
        # print('pattern:', pattern)
        # print('words:', words)

        if (not pattern) and (not words):
            return True

        if len(words) != len(pattern):
            return False
        # first char and all its occurences should be mapped to the same word
        c0 = pattern[0]
        word0 = words[0]
        occurs_of_first_char = self.find_occurs(c0, pattern)
        occurs_of_first_word = self.find_occurs(word0, words)
        # print('occurence of char in pattern', c0, ':', occurs_of_first_char)
        # print('occurence of word in pattern', word0, ':', occurs_of_first_word)

        if occurs_of_first_char != occurs_of_first_word:
            return False
        else:  # check remaining parts
            rem_pattern = self.drop_items_at_indices(pattern, occurs_of_first_char)
            rem_words = self.drop_items_at_indices(words, occurs_of_first_word)
            return self.follow_pattern(rem_pattern, rem_words)

    def wordPattern(self, pattern: str, s: str) -> bool:
        # there is a bijection between a letter in pattern and a non-empty word in str
        # so the number of letters in pattern must be equal to number of words in str
        # first letter in pattern will be mapped to the first word in str, so at all occurences of the first char, the same word must occur in the str

        words = str.split(s, ' ')
        return self.follow_pattern(pattern, words)


