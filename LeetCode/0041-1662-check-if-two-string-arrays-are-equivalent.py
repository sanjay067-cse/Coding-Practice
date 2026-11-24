# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        a = ""
        b = ""
        for w1 in word1:
            a += w1
        for w2 in word2:
            b += w2

        return a == b