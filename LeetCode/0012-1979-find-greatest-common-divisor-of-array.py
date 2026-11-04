# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        for i in range(smallest, 0, -1):
            if (smallest % i == 0) and (largest % i == 0):
                return i