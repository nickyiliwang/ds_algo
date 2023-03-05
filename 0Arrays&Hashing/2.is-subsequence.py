from collections import Counter
from typing import *
import os
os.system('clear')


# Counter doesn't account for order
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        for c in a:
            if (b[c] == 0):
                return False

        return True


s = "acb"
t = "ahbgdc"
Solution.isSubsequence(1, s, t,)

# # Counter doesn't account for order
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         a = Counter(s)
#         b = Counter(t)
#         for c in a:
#             if (b[c] == 0):
#                 return False

#         return True


# s = "acb"
# t = "ahbgdc"
# Solution.isSubsequence(1, s, t,)
