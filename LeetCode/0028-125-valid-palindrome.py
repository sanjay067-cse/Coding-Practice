# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for ch in s:
            if ch.isalnum():
                s1 += ch
        s2 = s1[ : : -1]
        return s1.lower() == s2.lower()