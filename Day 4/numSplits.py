class Solution:
    def numSplits(self, s: str) -> int:
        
        
        left  = [0] * len(s)
        right  = [0] * len(s)

        temp = []
        
        for i in range(0, len(s)):
            if s[i] not in temp:
                left[i] = left[i - 1] + 1
                temp.append(s[i])
            else:
                left[i] = left[i - 1]
        temp = []  
        right[-1] = 1
        temp.append(s[-1])
        for i in range(len(s) - 2, -1, -1):
            if s[i] not in temp:
                right[i] = right[i + 1] + 1
                temp.append(s[i])
            else:
                right[i] = right[i + 1]  
        count = 0
        for i in range(len(s) - 1):
            if left[i] == right[i + 1]:
                count += 1
    
        return count
