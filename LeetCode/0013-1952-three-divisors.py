# https://leetcode.com/problems/three-divisors/

class Solution:
    def isThree(self, n: int) -> bool:
        if n==1 or n==2: return False
        else:
            count = 0 
            for i in range(2, n):   # 1 & n will always be the divisor
                if n%i == 0:
                    count += 1
            
            if (count == 1): return True  
            else: return False    # means more than 1 divisor found 