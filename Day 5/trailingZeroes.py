class Solution:
    def trailingZeroes(self, n: int) -> int:       
        fac = 1
        
        for i in range(2, n + 1):
            fac *= i
        
        count = 0
        
        while fac % 10 == 0:
            count += 1
            fac //= 10
        
        return count
