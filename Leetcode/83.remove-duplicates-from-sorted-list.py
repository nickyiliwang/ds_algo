#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (51.81%)
# Likes:    8303
# Dislikes: 283
# Total Accepted:    1.4M
# Total Submissions: 2.7M
# Testcase Example:  '[1,1,2]'
#
# Given the head of a sorted linked list, delete all duplicates such that each
# element appears only once. Return the linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
#
#
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
#
#
#

from typing import *
from linked_list import LinkedList


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(val=None, next=head)
        prev, curr = dummy, head
        while curr:
            nextNode = curr.next
            if prev.val == curr.val:
                prev.next = nextNode
            else:
                prev = curr

            curr = curr.next
        return dummy.next


# @lc code=end

# Alternate more space efficient way of doing it.
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur = head
#         while cur:
#             while cur.next and cur.next.val == cur.val:
#                 cur.next = cur.next.next
#             cur = cur.next
#         return head


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)


node = Solution.deleteDuplicates("", linked_list.head.next)


while node:
    print(node.val)
    node = node.next
