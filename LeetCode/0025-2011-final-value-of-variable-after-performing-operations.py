# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X = 0 
        for operation in operations:
            if operation == "++X" or operation == "X++":
                X += 1
            if operation == "--X" or operation == "X--":
                X -= 1
        return X