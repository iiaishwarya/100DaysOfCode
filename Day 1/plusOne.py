class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        while i < len(digits):
            k = len(digits) - 1 - i
            if digits[k]  == 9:
                digits[k] = 0
            else:
                digits[k] += 1
                return digits
            i += 1
        
        return [1] + digits
                
