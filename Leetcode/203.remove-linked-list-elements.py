#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (47.82%)
# Likes:    7988
# Dislikes: 225
# Total Accepted:    1M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
#
#
# Example 1:
#
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
#
# Example 2:
#
#
# Input: head = [], val = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
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
    def removeElements(self, head, val):
        dummy = ListNode(next=head)

        prev, curr = dummy, head
        while curr:
            nextNode = curr.next

            if curr.val != val:
                prev = curr
            else:
                prev.next = nextNode

            curr = nextNode

        return dummy.next


# @lc code=end

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(6)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

node = Solution.removeElements("", linked_list.head.next, 6)

print(node)
while node:
    print(node.val)
    node = node.next
