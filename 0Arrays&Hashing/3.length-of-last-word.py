from collections import deque
from typing import *
import os
os.system('clear')


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        q = deque(s.split(" "))
        print(q)

        for i in range(len(q) - 1, -1, -1):
            if (q[i] != ""):
                return len(q[i])


print(
    Solution.lengthOfLastWord(1, "   fly me   to   the moon  "
                              )
)
