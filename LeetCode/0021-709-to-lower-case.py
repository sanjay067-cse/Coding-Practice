# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, s: str) -> str:
        lower = ""
        for ch in s:
            if ord(ch)<=90 and ord(ch)>=65:
                lower += chr(ord(ch) + 32) 
            else:
                lower += ch
        return lower