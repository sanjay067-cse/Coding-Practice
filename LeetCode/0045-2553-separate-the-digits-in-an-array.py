# https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = []
        for num in nums:
            temp = []
            while num > 0:
                d = num % 10
                temp.append(d)
                num = num // 10

            answer += temp[::-1]
        
        return answer