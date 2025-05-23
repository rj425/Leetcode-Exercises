# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        result = False
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if (flowerbed[i] == 0) and (flowerbed[i-1] == 0) and (flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                result = True
                break
        return result