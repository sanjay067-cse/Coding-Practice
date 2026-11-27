# https://leetcode.com/problems/minimum-number-game/

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort(reverse=True)
        while len(nums) != 0:
            alice = nums.pop(-1)
            bob = nums.pop(-1)
            arr.append(bob)
            arr.append(alice)
        return arr