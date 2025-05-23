# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()[::-1]
        s = ' '.join(s)
        return s
