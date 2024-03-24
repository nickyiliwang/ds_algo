#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (71.90%)
# Likes:    2640
# Dislikes: 355
# Total Accepted:    1.2M
# Total Submissions: 1.7M
# Testcase Example:  '3'
#
# Given an integer n, return a string array answer (1-indexed) where:
#
#
# answer[i] == "FizzB uzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
#
#
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output:
# ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

from typing import List


# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        # answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        # answer[i] == "Fizz" if i is divisible by 3.
        # answer[i] == "Buzz" if i is divisible by 5.
        # answer[i] == i (as a string) if none of the above conditions are true.
        for n in range(1, n + 1):
            if n % 3 == 0 and n % 5 == 0:
                res.append("FizzBuzz")
                continue
            elif n % 3 == 0:
                res.append("Fizz")
                continue
            elif n % 5 == 0:
                res.append("Buzz")
                continue
            else:
                res.append(str(n))

        return res


# @lc code=end

print(Solution().fizzBuzz(5))
# ["1","2","Fizz","4","Buzz"]
