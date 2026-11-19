# https://leetcode.com/problems/compute-alternating-sum/

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        alt_sum = 0
        for n in range(len(nums)):
            alt_sum += (-1)**n * nums[n]
            
        return alt_sum