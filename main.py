from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s) # Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})
        counter_t = Counter(t)

        for char in counter_t:
            if counter_t[char] > counter_s.get(char, 0):
                return char
        # diff = sum(ord(char) for char in t) - sum(ord(char) for char in s) // getting the difference between the sum of unicode points
        # return chr(diff)
