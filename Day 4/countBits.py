class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr = [0] * (n + 1)
        b = 1
        
        for i in range(1, n + 1):
            if i == b * 2:
                b *= 2
            
            arr[i] = arr[i - b] + 1
        
        return arr
