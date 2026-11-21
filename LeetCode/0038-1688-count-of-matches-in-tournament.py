# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            if n % 2 == 0:
                next = n // 2
                matches += next
            else:
                next = (n - 1) // 2
                matches += (n - 1) // 2 + 1

            n = next
            
        return matches