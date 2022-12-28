from typing import Optional
from ds_types.linked_list import LinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linkedListManipulate(head: Optional[ListNode]) -> Optional[ListNode]:
    node = ListNode(7, None)
    while head.next:
        head = head.next
    head.next = node


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linkedListManipulate(linked_list.head)
linked_list.display()
