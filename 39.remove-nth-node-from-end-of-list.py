from typing import Optional
from ds_types.linked_list import LinkedList


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # dummy is for when you want to remove any Node in the list, even if it's the head
    dummy = ListNode(0, head)

    slow, fast = dummy, head
    # 2 pointer
    # slow will be the node we remove while fast hits None
    for i in range(n):
        fast = fast.next
        
    # Also works
    # while fast and n > 0:
    #     fast = fast.next
    #     n -= 1
        
    while fast:
        slow = slow.next
        fast = fast.next

    # actually removing a node
    slow.next = slow.next.next

    return dummy.next


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
removeNthFromEnd(linked_list.head, 3)
# linked_list.display()
