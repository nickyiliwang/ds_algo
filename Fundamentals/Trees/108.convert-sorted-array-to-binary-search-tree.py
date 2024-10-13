#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (71.83%)
# Likes:    10860
# Dislikes: 554
# Total Accepted:    1.2M
# Total Submissions: 1.7M
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
#
# Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
#
#
# Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
#
#
#

# Key:
# recursively construct left and right partition by finding the mid point

# @lc code=start
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(nums[mid])

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(nums) - 1)


# @lc code=end

### Steps to Convert a Sorted Array into a Balanced BST

# 1. **Understand the properties**:
#    - A sorted array is given in ascending order.
#    - A BST requires each node to have all elements in the left subtree smaller and all elements in the right subtree larger than the node's value.

# 2. **Determine the root**:
#    - For a balanced BST, choose the middle element of the array as the root. This ensures that the left and right subtrees are balanced.

# 3. **Recursive division**:
#    - Recursively apply the same process to the left subarray and the right subarray to construct the left and right subtrees, respectively.

# 4. **Base case**:
#    - The recursion should stop when the subarray has no elements (i.e., when the start index exceeds the end index).

### Detailed Steps

# 1. **Start with the full array**:
#    - Identify the middle element of the array. This will be the root of your BST.
#    - For an array `arr` of length `n`, the middle index `mid` can be found as `mid = (start + end) // 2` where `start` is the starting index and `end` is the ending index.

# 2. **Create the root node**:
#    - Create a tree node with the middle element.

# 3. **Construct the left subtree**:
#    - Recursively apply the process to the left subarray (`arr[start:mid-1]`).

# 4. **Construct the right subtree**:
#    - Recursively apply the process to the right subarray (`arr[mid+1:end]`).

# 5. **Combine the subtrees**:
#    - Attach the left and right subtrees to the root node.

### Explanation of the Example

# 1. **Find the middle element**:
#    - For `arr = [-10, -3, 0, 5, 9]`, the middle element is `0`.

# 2. **Create the root node**:
#    - `0` becomes the root.

# 3. **Recursively construct left and right subtrees**:
#    - Left subtree with `arr = [-10, -3]`
#    - Right subtree with `arr = [5, 9]`

# 4. **Repeat the process** for each subtree until the entire array is converted into a BST.

# By following these steps, you can systematically convert any sorted array into a balanced BST.

