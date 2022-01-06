class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x: x[1])      
        cur, res = float('-inf'), 0
        for p in pairs:
            if cur < p[0]: 
                cur = p[1]
                res += 1
        return res
