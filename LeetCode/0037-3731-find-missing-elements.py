# https://leetcode.com/problems/find-missing-elements/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
            a = min(nums)
            b = max(nums)
            missing_list = []
            for i in range(a, b+1):
                if i not in nums:
                    missing_list.append(i)
            return missing_list