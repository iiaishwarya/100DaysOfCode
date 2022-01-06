class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                x = nums[i]
                nums[i] += (nums[i-1] - nums[i]) + 1
                steps += nums[i] - x
        return steps
        
