# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result