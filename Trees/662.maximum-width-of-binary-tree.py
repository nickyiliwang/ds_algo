#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (43.01%)
# Likes:    8632
# Dislikes: 1194
# Total Accepted:    378.7K
# Total Submissions: 880.4K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given the root of a binary tree, return the maximum width of the given tree.
#
# The maximum width of a tree is the maximum width among all levels.
#
# The width of one level is defined as the length between the end-nodes (the
# leftmost and rightmost non-null nodes), where the null nodes between the
# end-nodes that would be present in a complete binary tree extending down to
# that level are also counted into the length calculation.
#
# It is guaranteed that the answer will in the range of a 32-bit signed
# integer.
#
#
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4
# (5,3,null,9).
#
#
# Example 2:
#
#
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7
# (6,null,null,null,null,null,7).
#
#
# Example 3:
#
#
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2
# (3,2).
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)]) # (node, level)
        res = 0

        while q:
            # idx of last element - first + 1 => width
            res = max(res, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                node, i = q.popleft()
                if node.left:
                    q.append((node.left, 2 * i))
                if node.right:
                    q.append((node.right, 2 * i + 1))
        return res


# @lc code=end


# ```
#         1
#        / \
#       2   3
#      /     \
#     4       5
# ```

# Here’s how the algorithm works step-by-step:

# ### Initial Setup
# 1. Initialize a deque `q` with the root node and its index (0), i.e., `q = deque([(root, 0)])`.
# 2. Initialize `res` to 0 to keep track of the maximum width.

# ### Level 1
# - **Queue at start**: `[(1, 0)]` (node 1 at index 0)
# - **Width calculation**: `q[-1][1] - q[0][1] + 1 = 0 - 0 + 1 = 1`
# - **Update `res`**: `res = max(res, 1) = 1`
# - **Process nodes**:
#   - Dequeue node 1 at index 0.
#   - Enqueue left child (node 2) at index `2*0 = 0` and right child (node 3) at index `2*0 + 1 = 1`.
# - **Queue after processing**: `[(2, 0), (3, 1)]`

# ### Level 2
# - **Queue at start**: `[(2, 0), (3, 1)]`
# - **Width calculation**: `q[-1][1] - q[0][1] + 1 = 1 - 0 + 1 = 2`
# - **Update `res`**: `res = max(res, 2) = 2`
# - **Process nodes**:
#   - Dequeue node 2 at index 0.
#     - Enqueue left child (node 4) at index `2*0 = 0` (no right child).
#   - Dequeue node 3 at index 1.
#     - Enqueue right child (node 5) at index `2*1 + 1 = 3` (no left child).
# - **Queue after processing**: `[(4, 0), (5, 3)]`

# ### Level 3
# - **Queue at start**: `[(4, 0), (5, 3)]`
# - **Width calculation**: `q[-1][1] - q[0][1] + 1 = 3 - 0 + 1 = 4`
# - **Update `res`**: `res = max(res, 4) = 4`
# - **Process nodes**:
#   - Dequeue node 4 at index 0 (no children).
#   - Dequeue node 5 at index 3 (no children).
# - **Queue after processing**: `[]` (empty queue)

# ### Final Result
# Since the queue is empty, we exit the loop and return the result, which is `4`.

# ### Summary
# The algorithm processes the binary tree level by level, tracking the width of each level using the indices of the nodes. It uses a deque to manage the nodes at each level and their indices, calculating the width as the difference between the indices of the last and first nodes at each level plus one. The maximum width found during these calculations is returned as the final result.

# In this example, the maximum width is 4, which is at the third level of the tree.