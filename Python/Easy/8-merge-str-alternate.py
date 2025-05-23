# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shortest = len(word1) if len(word1) < len(word2) else len(word2)
        resultString = ''
        for i in range(shortest):
            resultString += word1[i]
            resultString += word2[i]
        resultString += word1[i+1:] if len(word1) > len(word2) else word2[i+1:]
        return resultString