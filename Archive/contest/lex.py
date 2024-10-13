class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        count = 0

        for i in range(n - 1):
            if count == 1:
                break
            if int(s[i]) % 2 == int(s[i + 1]) % 2:
                if s[i] > s[i + 1]:
                    s[i], s[i + 1] = s[i + 1], s[i]
                    count += 1

        return "".join(s)
