#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (51.38%)
# Likes:    15588
# Dislikes: 840
# Total Accepted:    1.7M
# Total Submissions: 3.2M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in O(n) time and O(1) space?
#
from typing import *
from linked_list import LinkedList


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        # mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev, curr = None, slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # find result
        left, right = head, prev

        # right should be the longer
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


# @lc code=end

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(2)
linked_list.append(2)
linked_list.append(1)

print(Solution.isPalindrome("", linked_list.head.next))


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        curr = head

        while curr:
            list.append(curr.val)
            curr = curr.next

        left, right = 0, len(list) - 1

        while left < right:
            if list[left] != list[right]:
                return False
            left += 1
            right -= 1

        return True
