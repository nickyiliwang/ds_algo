from typing import Optional
from ds_types.linked_list import LinkedList

# @lc app=leetcode id=19 lang=python3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow, fast = dummy, head
        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        # removing a node
        slow.next = slow.next.next

        return dummy.next


# @lc code=end


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
removeNthFromEnd(linked_list.head, 3)
# linked_list.display()
