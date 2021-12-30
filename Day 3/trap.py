class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]
        for i in range(1,n):
            left_max[i] = max(left_max[i - 1], height[i])
            
        for k in range(n - 2, -1, -1):
            right_max[k] = max(right_max[k + 1], height[k])
        
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
            
        return ans
