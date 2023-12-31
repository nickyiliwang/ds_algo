#
# @lc app=leetcode id=2130 lang=python
#
# [2130] Maximum Twin Sum of a Linked List
#
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
#
# algorithms
# Medium (81.31%)
# Likes:    3255
# Dislikes: 85
# Total Accepted:    225.6K
# Total Submissions: 277.4K
# Testcase Example:  '[5,4,2,1]'
#
# In a linked list of size n, where n is even, the i^th node (0-indexed) of the
# linked list is known as the twin of the (n-1-i)^th node, if 0 <= i <= (n / 2)
# - 1.
#
#
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the
# twin of node 2. These are the only nodes with twins for n = 4.
#
#
# The twin sum is defined as the sum of a node and its twin.
#
# Given the head of a linked list with even length, return the maximum twin sum
# of the linked list.
#
#
# Example 1:
#
#
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum
# = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6.
#
#
# Example 2:
#
#
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
#
#
# Example 3:
#
#
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 +
# 100000 = 100001.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is an even integer in the range [2,
# 10^5].
# 1 <= Node.val <= 10^5
#
#
#

from linked_list import LinkedList


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        prev = None
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next

            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        result = -1

        while slow:
            result = max(result, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return result


# @lc code=end


linked_list = LinkedList()
linked_list.append(5)
linked_list.append(4)
linked_list.append(2)
linked_list.append(1)

print(Solution.pairSum("", linked_list.head.next))


# Less efficient, but more understandable with 2 pointer
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr = head
        nums = []
        result = -1

        while curr:
            nums.append(curr.val)
            curr = curr.next

        left, right = 0, len(nums) - 1

        while left < right:
            result = max(nums[left] + nums[right], result)
            left += 1
            right -= 1

        return result
