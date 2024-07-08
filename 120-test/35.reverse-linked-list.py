# @lc app=leetcode id=206 lang=python3
from typing import Optional
from ds_types.linked_list import LinkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Key:
# save the next node as temp value
# point the next node to prev node
# move the prev pointer forward to curr for next loop
# move the curr pointer forward to temp/next value for next loop


# @lc code=start
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

# @lc code=end
