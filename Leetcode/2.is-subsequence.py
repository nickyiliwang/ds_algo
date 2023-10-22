from collections import deque
from typing import *
import os
os.system('clear')


# FIFO Queue
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = deque(s)
        for c in t:
            if q and c == q[0]:
                q.popleft()

        if len(q) > 0:
            return False
        else:
            return True


s = "abc"
t = "ahbgdc"
print(
    Solution.isSubsequence(1, s, t,)
)

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
