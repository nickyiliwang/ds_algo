from typing import *
from collections import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        needCount, haveCount = Counter(t), Counter()
        needLen, haveLen = len(t), 0
        res, resLen = "", float("inf")

        for right in range(len(s)):
            haveCount[s[right]] += 1

            if haveCount[s[right]] <= needCount[s[right]]:
                haveLen += 1

            while haveLen == needLen:
                if right - left + 1 < resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1

                haveCount[s[left]] -= 1
                if haveCount[s[left]] < needCount[s[left]]:
                    haveLen -= 1

                left += 1

        return res

# Explanation


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        needCount, haveCount = Counter(t), Counter()
        needLen, haveLen = len(t), 0
        # Need the resLen large so the first long result length we find will be smaller and replace it
        res, resLen = "", float("inf")

        # Extend window
        for right in range(len(s)):

            haveCount[s[right]] += 1

            # why not exact but instead: "<="
            # We need to increment the len 1 by 1
            if haveCount[s[right]] <= needCount[s[right]]:
                haveLen += 1

            # window found !
            while haveLen == needLen:
                # Found a result with shorter length
                if right - left + 1 < resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1

                # Shrinking window and updating
                haveCount[s[left]] -= 1
                # we don't care if have count of the left window has more than we need
                if haveCount[s[left]] < needCount[s[left]]:
                    haveLen -= 1

                left += 1

        return res


# Method 2


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = Counter(t), Counter()
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
