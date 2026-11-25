# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            dig_sum = 0
            num = nums[i]
            while num > 0:
                d = num % 10
                dig_sum += d
                num = num // 10
            if dig_sum == i:
                return i

        return -1