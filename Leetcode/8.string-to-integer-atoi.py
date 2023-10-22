#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (16.76%)
# Likes:    3855
# Dislikes: 11954
# Total Accepted:    1.3M
# Total Submissions: 8M
# Testcase Example:  '"42"'
#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit
# signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-'
# or '+'. Read this character in if it is either. This determines if the final
# result is negative or positive respectively. Assume the result is positive if
# neither is present.
# Read in next the characters until the next non-digit character or the end of
# the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no
# digits were read, then the integer is 0. Change the sign as necessary (from
# step 2).
# If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
# then clamp the integer so that it remains in the range. Specifically,
# integers less than -2^31 should be clamped to -2^31, and integers greater
# than 2^31 - 1 should be clamped to 2^31 - 1.
# Return the integer as the final result.
#
#
# Note:
#
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of
# the string after the digits.
#
#
#
# Example 1:
#
#
# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the
# current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
# ⁠        ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
# ⁠        ^
# Step 3: "42" ("42" is read in)
# ⁠          ^
# The parsed integer is 42.
# Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.
#
#
# Example 2:
#
#
# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
# ⁠           ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
# ⁠            ^
# Step 3: "   -42" ("42" is read in)
# ⁠              ^
# The parsed integer is -42.
# Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.
#
#
# Example 3:
#
#
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading
# whitespace)
# ⁠        ^
# Step 2: "4193 with words" (no characters read because there is neither a '-'
# nor '+')
# ⁠        ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next
# character is a non-digit)
# ⁠            ^
# The parsed integer is 4193.
# Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ',
# '+', '-', and '.'.

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # My solution
        num = ""
        op = ""

        for char in s:
            if char != " ":
                if (char == "+" or char == "-") and num == "":
                    op += char
                    if (len(op) > 1):
                        return 0
                elif (char == "+" or char == "-") and len(num) > 0:
                    break
                    # return 0
                elif char.isnumeric() or (char == "."):
                    if (char == "."):
                        break
                    else:
                        num += char

                elif (char.isalpha() or char == ".") and num == "":
                    return 0
                elif (char.isalpha()) and len(num) > 0:
                    break
            if char == " " and (len(num) > 0 or len(op) > 0):
                break

        if num == "":
            num = 0

        if op == "":
            op = "+"

        if (op == "-"):
            if (-abs(int(num)) < (-2 ** 31)):
                return (-2 ** 31)
            else:
                return -abs(int(num))
        else:
            if (int(num) > (2 ** 31 - 1)):
                return (2 ** 31 - 1)
            else:
                return int(num)


# @lc code=end
print(Solution.myAtoi("", "  +  413"))

# More logical solution
# https://www.youtube.com/watch?v=zwZXiutgrUE

# My solution
# 1086/1086 cases passed (45 ms)
# Your runtime beats 37.68 % of python3 submissions
# Your memory usage beats 98.42 % of python3 submissions (16.1 MB)
