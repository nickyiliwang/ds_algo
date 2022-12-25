# yapf: disable
from typing import Optional
from linked_list import LinkedList

# yapf: enable


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# two pointers
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.display()

reversed = reverseList(linked_list.head)

print(reversed.val)
