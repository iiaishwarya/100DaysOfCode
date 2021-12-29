class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxAmount(i):
            if i >= len(nums):
                return 0
            
            if memo[i] > -1:
                return memo[i]
            
            memo[i] = max(maxAmount(i + 1), maxAmount( i + 2) + nums[i])
            return memo[i]
            

        memo = [-1] * len(nums)   
        return maxAmount(0)
