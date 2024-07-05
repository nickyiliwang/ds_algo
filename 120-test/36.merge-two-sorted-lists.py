# @lc app=leetcode id=21 lang=python3
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # avoid initial empty list edge case by having a dummy
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            # need to keep sorted order
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # appending what's left of either list
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # dummy is in the beginning of the list
        return dummy.next


# @lc code=end
