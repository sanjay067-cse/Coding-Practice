# https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution:
    def coloredCells(self, n: int) -> int:
        return (n**2 + (n-1)**2)