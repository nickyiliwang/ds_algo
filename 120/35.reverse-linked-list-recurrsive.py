from typing import Optional
from ds_types.linked_list import LinkedList

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# two pointers


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # recursive: T O(n), M O(n)
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead

    # -> 1 size one, if head.next will not execute
    # 1 -> 2 -> None


linked_list = LinkedList()
print('head val', linked_list.head.val)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.display()

reversed = reverseList(linked_list.head)

print(reversed.val)
