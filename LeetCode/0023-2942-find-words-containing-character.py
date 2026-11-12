# https://leetcode.com/problems/find-words-containing-character/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index = []
        for i in range(0, len(words)):
            if x in words[i]:
                index.append(i)
        return index