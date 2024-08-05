# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (48.70%)
# Likes:    7666
# Dislikes: 14683
# Total Accepted:    1.4M
# Total Submissions: 2.9M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
#
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# Example 3:
#
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
#
#

# P   A   H   N
# A P L S I I G
# Y   I   R


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        graph = [[] for _ in range(numRows)]
        rowIdx = 0

        for i, n in enumerate(s):
            if rowIdx % numRows +1 == 0:


            graph[rowIdx % numRows].append(n)
            rowIdx += 1

        print(graph)

        # [["P", "P", "I", "I", "N"], ["A", "A", "S", "R", "G"], ["Y", "L", "H", "I"]]


# @lc code=end

print(Solution().convert("PAYPALISHIRING", 3))

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"z
