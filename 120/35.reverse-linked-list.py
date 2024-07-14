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
        prev, curr = None, head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev


# @lc code=end

# recursive
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

