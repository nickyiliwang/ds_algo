# Definition for singly-linked list.
from typing import *
from collections import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        delete_me = set(nums)

        while curr.next:
            if curr.next.val in delete_me:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
            

