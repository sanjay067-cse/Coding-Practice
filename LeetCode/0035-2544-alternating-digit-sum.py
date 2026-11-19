# https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num = str(n)
        alt_digit_sum = 0
        for i in range(len(num)):
            alt_digit_sum += (-1)**i * int(num[i])

        return alt_digit_sum