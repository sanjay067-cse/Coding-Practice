# https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        total = 0
        count = Counter(nums)
        for num in count:
            if count[num] == 1:
                total += num

        return total