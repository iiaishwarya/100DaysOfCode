class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        subset = total // 2
        
        dp = [ [False] * (subset + 1) for _ in range(len(nums) + 1) ]
        
        dp[0][0] = True
        
        for i in range(1, len(nums) + 1):
            curr = nums[i - 1]
            
            for j in range(subset + 1):
                dp[i][j] = dp[i - 1][j] if j < curr else (dp[i - 1][j] or dp[i - 1][j - curr])
                
        return dp[len(nums)][subset]
                    
