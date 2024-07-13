# @lc app=leetcode id=143 lang=python3
from typing import Optional
from ds_types.linked_list import LinkedList, ListNode

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# @lc code=start
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

# @lc code=end

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

# Starting at 1 instead of 0 with list1.head.next
Solution().reorderList(linked_list.head.next)


current = linked_list.head
while current is not None:
    print(current.val)  # Do something with the value
    current = current.next
