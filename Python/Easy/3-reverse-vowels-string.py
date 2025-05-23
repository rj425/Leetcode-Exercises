# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        vowels = list('aeiouAEIOU')
        left, right = 0, len(word)-1
        while left < right:
            while left < right and word[left] not in vowels:
                left += 1
            while left < right and word[right] not in vowels:
                right -= 1
            word[left], word[right] = word[right], word[left]
            left +=1
            right -=1
        word = ''.join(word)
        return word