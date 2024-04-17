# Combinatorial Example Problem
# Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

# Input: 2
# Output: ["aa", "ab", "ba", "bb"]

# Input: 4
# Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]

import string


# function dfs(start_index, path):
#   if is_leaf(start_index):
#     report(path)
#     return
#   for edge in get_edges(start_index):
#     path.add(edge)
#     dfs(start_index + 1, path)
#     path.pop()


class Solution:
    def backtracking_combinatorial(self, num):
        letters = string.ascii_lowercase[:num]
        res = set()

        def dfs(i, path):
            if len(path) == num:
                res.add(path)
                return

            for char in letters:
                path += char
                dfs(i + 1, path)
                path = path[:-1]

        dfs(0, "")
        return res


print(Solution().backtracking_combinatorial(4))
