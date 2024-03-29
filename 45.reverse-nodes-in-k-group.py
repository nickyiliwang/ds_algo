from typing import Optional, List
from ds_types.linked_list import LinkedList, ListNode


# My solution, not optimized because using extra spaces (lists) to store, general logic seems intuitive.
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        twoDList = []
        tempK = k
        temp = []

        current = head

        while current != None:
            if tempK != 0:
                temp.append(current.val)
                tempK -= 1
            else:
                twoDList.append(temp)
                temp = [current.val]
                tempK = k - 1

            current = current.next

        twoDList.append(temp)
        temp = []

        for list in twoDList:
            if len(list) == k:
                for n in reversed(list):
                    temp.append(n)
            else:
                for n in list:
                    temp.append(n)

        current = dummy

        for n in temp:
            current.next = ListNode(n)
            current = current.next

        return dummy.next


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

current = Solution.reverseKGroup("", linked_list.head.next, 2)
print(current.next.val)


# Cool recursive solution
#
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         # Check if we need to reverse the group
#         curr = head
#         for _ in range(k):
#             if not curr: return head
#             curr = curr.next


#         # Reverse the group (basic way to reverse linked list)
#         prev = None
#         curr = head
#         for _ in range(k):
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt


#       # After reverse, we know that `head` is the tail of the group.
# 		# And `curr` is the next pointer in original linked list order
#         head.next = self.reverseKGroup(curr, k)
#         return prev
