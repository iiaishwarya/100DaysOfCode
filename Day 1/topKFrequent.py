class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}
        for num in nums:
            if num in obj:
                obj[num] += 1
            else:
                obj[num] = 1

        lst = sorted(obj.keys(), key = lambda x : -obj[x])
        return lst[0: k ]
