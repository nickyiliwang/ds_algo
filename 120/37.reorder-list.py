from typing import Optional
from ds_types.linked_list import LinkedList, ListNode

# @lc app=leetcode id=143 lang=python3


# @lc code=start
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # phase 1
        # using Slow Fast Algo to divide the list into 2 parts
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # phase 2
        # reverse second half
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # phase 3
        # rearrange the 2 parts into desired linked list
        # only need to go as far as the second half
        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp


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
