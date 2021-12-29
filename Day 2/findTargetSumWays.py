class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # self.count = 0
        
        def recursion(index, total, memo):
            
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            else:      
                if memo[index][sum(nums) + total] != None:
                    return memo[index][sum(nums) + total]
                add = recursion(index + 1, total + nums[index], memo)
                sub = recursion(index + 1,  total - nums[index], memo)
                memo[index][sum(nums) + total] = add + sub
                return memo[index][sum(nums) + total]
            
        memo = [[None] * (2 * sum(nums) + 1) for _ in range(len(nums) )]
        print(memo)
        return recursion(0, 0, memo)
        # return self.count
        
