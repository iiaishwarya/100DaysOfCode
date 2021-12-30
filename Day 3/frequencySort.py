class Solution:
    def frequencySort(self, s: str) -> str:
        obj = {}
        
        s = sorted(s)
        for ch in s:
            if ch in obj:
                obj[ch] += 1
            else:
                obj[ch] = 1
        return sorted(s, key=lambda x: -obj[x])
