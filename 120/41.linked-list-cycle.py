from ds_types.linked_list import LinkedList, ListNode
from typing import Optional

# @lc app=leetcode id=141 lang=python3

# Time: O(1), Space: O(1)
# Tortoise and Hare
# while loop only tracks the hare


# @lc code=start
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# @lc code=end
