# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = Counter(nums)
        good_pairs = 0
        for n in freq.values():
            good_pairs += n * (n-1)//2
        return good_pairs