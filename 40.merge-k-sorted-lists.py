from typing import Optional
from typing import List
from ds_types.linked_list import LinkedList

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # checking for empty array edge cases
        if not lists or len(lists) == 0:
            return None

        # phase 1
        # merge sorted lists
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # ensure we only process and merge even lists
                l2 = lists[i + 1] if len(lists) > (i + 1) else None

                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    # mergeList only need to merge 2 lists and produce 1
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next


# class Solution:

#     def mergeKLists(self,
#                     lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         # edge case
#         if not lists or len(lists) == 0:
#             return None

#         #
#         while len(lists) > 1:
#             mergedLists = []

#             # like merge sort
#             # doing so will eliminate redundancy
#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if (i + 1) < len(lists) else None

#                 mergedLists.append(self.mergeList(l1, l2))
#             lists = mergedLists
#         return lists[0]

#     def mergeList(self, l1, l2):
#         dummy = ListNode()
#         tail = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next

#         if l1:
#             tail.next = l1
#         if l2:
#             tail.next = l2

#         return dummy.next

list = []
linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(4)
linked_list_1.append(5)
linked_list_2 = LinkedList()
linked_list_2.append(1)
linked_list_2.append(3)
linked_list_2.append(4)
linked_list_3 = LinkedList()
linked_list_3.append(2)
linked_list_3.append(6)
linked_list_1.display()
linked_list_2.display()
linked_list_3.display()
list.append(linked_list_1.head)
list.append(linked_list_2.head)
list.append(linked_list_3.head)

mergeKListsInstance = Solution()

newList = mergeKListsInstance.mergeKLists(list)

while newList:
    print(newList.val)
    newList = newList.next