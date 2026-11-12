# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        answer = []
        for i in range(0, len(boxes)):
            move = 0
            for j in range(0 , len(boxes)):
                if boxes[j] == "1":
                    move += abs(i-j)
            answer.append(move)
        return answer