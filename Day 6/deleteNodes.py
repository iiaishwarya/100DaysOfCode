class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        keep = 0
        delete = 0
        prev = head
        curr = head
        while curr:
            keep = 0
            delete = 0   
            while curr and keep != m:
                prev = curr
                curr = curr.next
                keep += 1
            
            while curr and delete != n:
                curr = curr.next
                delete += 1
            
            prev.next = curr
            
        return head
