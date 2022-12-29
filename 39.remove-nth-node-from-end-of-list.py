from typing import Optional
from ds_types.linked_list import LinkedList


# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # dummy is for when you want to remove any Node in the list, even if it's the head
    dummy = ListNode(0, head)

    left, right = dummy, head
    # 2 pointer
    # left will be the node we remove while right hits None
    while right.next is not None and n != 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # actually removing a node
    left.next = left.next.next
    
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
