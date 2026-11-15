# https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        mp = {}
        p_diff = 0
        for i in range(len(s)):
            mp[s[i]] = i
        for i in range(len(t)):
            p_diff += abs(i - mp[t[i]])
        return p_diff