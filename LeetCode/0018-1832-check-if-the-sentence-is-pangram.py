# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        letters = [False]*26
        for ch in sentence:
            index = ord(ch) - ord('a')
            letters[index] = True
        return all(letters)