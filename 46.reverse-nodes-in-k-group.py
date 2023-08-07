from typing import Optional, List
from ds_types.linked_list import LinkedList, ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        nodeCount = -1 # not counting head with 0
        
        current = head
        
        while current != None:
            nodeCount += 1
            print(current.val)
            current = current.next
            
            


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

Solution.reverseKGroup("", linked_list.head, 2)