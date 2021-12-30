class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        point = head
        count = 0
        while point:
            count += 1
            point = point.next
        
        mid = count // 2 if count % 2 != 0 else count / 2 
        while mid != 0:
            head = head.next
            mid -= 1
        
        return (head)
