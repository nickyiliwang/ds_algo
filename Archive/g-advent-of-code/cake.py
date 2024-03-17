def solution(s):
    def countOccurrence(s, pattern):
        count = 0
        left, right = 0, len(pattern)
        while right <= len(s):
            if s[left:right] == pattern:
                count += 1
                left = right
                right += len(pattern)
            else:
                right += 1

        return count

    for i in range(1, len(s) + 1):
        substr = s[:i]

        count = countOccurrence(s, substr)

        if count * i == len(s):
            return count


print(solution("aaaaabaaaaab"))
