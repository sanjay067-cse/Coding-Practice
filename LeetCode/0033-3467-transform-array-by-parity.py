# https://leetcode.com/problems/transform-array-by-parity/

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ptr = 0

        for num in nums:
            if num % 2 == 0:
                nums[ptr] = 0
                ptr += 1 

        for i in range(ptr, len(nums)):
            nums[i] = 1

        return nums