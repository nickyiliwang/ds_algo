from typing import *
from ds_types.linked_list import ListNode

# @lc app=leetcode id=2 lang=python3

# Example 1:
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#


# @lc code=start
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1str = l2str = ""

        # phase 1
        # get the numbers by flipping the order of appending
        while l1:
            l1str = str(l1.val) + l1str
            l1 = l1.next
        while l2:
            l2str = str(l2.val) + l2str
            l2 = l2.next

        # phase 2
        sum = str(int(l1str) + int(l2str))

        dummy = ListNode()
        curr = dummy

        for n in reversed(sum):
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next


# @lc code=end
