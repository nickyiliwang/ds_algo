from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# two pointers


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # prev node is Null
    # curr to the first node / head
    prev, curr = None, head

    while curr is not None:
        nextPointer = curr.next
        curr.next = prev
        prev = curr
        curr = nextPointer

    return prev
