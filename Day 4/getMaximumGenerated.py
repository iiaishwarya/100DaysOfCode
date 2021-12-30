class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n == 0:
            return 0
    
        arr = [0] * ( n + 1)
        
        arr[0] = 0
        arr[1] = 1
        m = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                arr[i] = arr[int(i / 2)]
            else:
                arr[i] = arr[int(i // 2)] + arr[int(i// 2) + 1]
            m = max(arr[i], m)
        return m
