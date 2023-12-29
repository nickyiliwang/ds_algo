#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (56.46%)
# Likes:    14371
# Dislikes: 1279
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no
# intersection at all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:
#
# The test cases are generated such that there are no cycles anywhere in the
# entire linked structure.
#
# Note that the linked lists must retain their original structure after the
# function returns.
#
# Custom Judge:
#
# The inputs to the judge are given as follows (your program is not given these
# inputs):
#
#
# intersectVal - The value of the node where the intersection occurs. This is 0
# if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head)
# to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head)
# to get to the intersected node.
#
#
# The judge will then create the linked structure based on these inputs and
# pass the two heads, headA and headB to your program. If you correctly return
# the intersected node, then your solution will be accepted.
#
#
# Example 1:
#
#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as
# [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are
# 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with
# value 1 in A and B (2^nd node in A and 3^rd node in B) are different node
# references. In other words, they point to two different locations in memory,
# while the nodes with value 8 in A and B (3^rd node in A and 4^th node in B)
# point to the same location in memory.
#
#
# Example 2:
#
#
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as
# [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node
# before the intersected node in B.
#
#
# Example 3:
#
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it
# reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
#
# Constraints:
#
#
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB
# intersect.
#
#
#
# Follow up: Could you write a solution that runs in O(m + n) time and use only
# O(1) memory?
#

from typing import *
from linked_list import LinkedList


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        one, two = headA, headB

        while one != two:
            one = one.next if one else headB
            two = two.next if two else headA

        return one


# @lc code=end

linked_listA = LinkedList()
linked_listA.append(4)
linked_listA.append(1)
linked_listA.append(8)
linked_listA.append(4)
linked_listA.append(5)

linked_listB = LinkedList()
linked_listB.append(5)
linked_listB.append(6)
linked_listB.append(1)
linked_listB.append(8)
linked_listB.append(4)
linked_listB.append(5)

node = Solution.getIntersectionNode("", linked_listA.head.next, linked_listB.head.next)

print(node.val)

# Visualization
# Visualization of this solution:
# Case 1 (Have Intersection & Same Len):

#        a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#        b
#             a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#             b
#                  a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#                  b
# A:     a1 → a2 → a3
#                    ↘ a
#                      c1 → c2 → c3 → null
#                    ↗ b
# B:     b1 → b2 → b3
# Since a == b is true, end loop while(a != b), return the intersection node a = c1.

# Case 2 (Have Intersection & Different Len):

#             a
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#        b
#                  a
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#             b
# A:          a1 → a2
#                    ↘ a
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#                  b
# A:          a1 → a2
#                    ↘      a
#                      c1 → c2 → c3 → null
#                    ↗ b
# B:     b1 → b2 → b3
# A:          a1 → a2
#                    ↘           a
#                      c1 → c2 → c3 → null
#                    ↗      b
# B:     b1 → b2 → b3
# A:          a1 → a2
#                    ↘                a = null, then a = b1
#                      c1 → c2 → c3 → null
#                    ↗           b
# B:     b1 → b2 → b3
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗                b = null, then b = a1
# B:     b1 → b2 → b3
#        a
#             b
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#             a
#                  b
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#                  a
# A:          a1 → a2
#                    ↘ b
#                      c1 → c2 → c3 → null
#                    ↗ a
# B:     b1 → b2 → b3
# Since a == b is true, end loop while(a != b), return the intersection node a = c1.

# Case 3 (Have No Intersection & Same Len):

#        a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#        b
#             a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#             b
#                  a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#                  b
#                       a = null
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#                       b = null
# Since a == b is true (both refer to null), end loop while(a != b), return a = null.

# Case 4 (Have No Intersection & Different Len):

#        a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#        b
#             a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#             b
#                  a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                  b
#                       a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                       b = null, then b = a1
#        b                   a = null, then a = b1
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#             b
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#        a
#                  b
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#             a
#                       b
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                  a
#                            b = null
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                       a = null
# Since a == b is true (both refer to null), end loop while(a != b), return a = null.

# Notice that if list A and list B have the same length, this solution will terminate in no more than 1 traversal; if both lists have different lengths, this solution will terminate in no more than 2 traversals -- in the second traversal, swapping a and b synchronizes a and b before the end of the second traversal. By synchronizing a and b I mean both have the same remaining steps in the second traversal so that it's guaranteed for them to reach the first intersection node, or reach null at the same time (technically speaking, in the same iteration) -- see Case 2 (Have Intersection & Different Len) and Case 4 (Have No Intersection & Different Len).

# WIP my solution
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         lengthA, lengthB = 0, 0

#         curr = headA
#         while curr:
#             lengthA += 1
#             curr = curr.next

#         curr = headB
#         while curr:
#             lengthB += 1
#             curr = curr.next

#         diff = abs(lengthA - lengthB)

#         if lengthA > lengthB:
#             headACurr, headBCurr = headA, headB
#             while diff != 0:
#                 headACurr = headACurr.next
#                 diff -= 1

#             while headACurr and headBCurr:
#                 if headACurr.val == headBCurr.val:
#                     return headACurr
#                 else:
#                     headACurr = headACurr.next
#                     headBCurr = headBCurr.next
#         else:
#             headACurr, headBCurr = headA, headB

#             while diff != 0:
#                 headBCurr = headBCurr.next
#                 diff -= 1

#             while headACurr and headBCurr:
#                 if headACurr.val == headBCurr.val:
#                     return headBCurr
#                 else:
#                     headACurr = headACurr.next
#                     headBCurr = headBCurr.next
#         return None
