# https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution:
    def reverseDegree(self, s: str) -> int:
        rev_deg = 0
        for i in range(len(s)):
            rev_deg += (ord('z') - ord(s[i]) +1) * (i+1)

        return rev_deg