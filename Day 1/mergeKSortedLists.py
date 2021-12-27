class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        
        i = 1
        
        while i < n:
            for k in range(0, n - i, i * 2):
                print(i, k)
                lists[k] = self.merge2Lists(lists[k], lists[i + k])
            i *= 2
        return lists[0] if len(lists) > 0 else None
    
    def merge2Lists(self, list1, list2):
        
        p1 = p2 = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                p2.next = list1
                list1 = list1.next
            else:
                p2.next = list2
                list2 = list1
                list1 = p2.next.next
                
            p2 = p2.next
        
        if not list1:
            p2.next = list2
        
        if not list2:
            p2.next = list1
        
        return p1.next
            
        
