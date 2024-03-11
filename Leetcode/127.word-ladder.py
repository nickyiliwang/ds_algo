#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (38.84%)
# Likes:    11750
# Dislikes: 1863
# Total Accepted:    1M
# Total Submissions: 2.7M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
#
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
#
#
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
# -> "dog" -> cog", which is 5 words long.
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
#
#
#
# Constraints:
#
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
#
#
#

from typing import List


# BigO n^2 * M
# hot: *ot, h*t, ho*
# dot: *ot, d*t, do*
# lot: *ot, l*t, lo*
# {*ot: [hot, dot, lot]}

# KEY:
# word[:i] + "*" + word[i + 1:]

from collections import defaultdict, deque


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        # build adjacency list
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                nei[pattern].append(word)

        visited = set()
        q = deque([beginWord])
        res = 1

        # BFS check each layer to find the endWord
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                # Build pattern
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    # Ref pattern in adjList, only want unvisited
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0


# @lc code=end

print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# OUTPUT: 5

# 											 hit, level = 1
# 								 /            |              \
# 					     *it                h*t                  hi*
# 						   |                 |                     |
# 			             null  	       hot ,level = 2      null
# 										 /   |   \
# 										/    |     \
# 				               *ot           h*t      ho*
# 				           /    |   \         |        |
#                      hot,2   dot,3  lot,3   hot,2    hot,2


# # as we can see,  "hot" has been visited in level 2, but "hot" will still appear at the next level.
# # To avoid duplicate calculation,
# # we keep a visited map,
# # if the word in the visited map, we skip the word, i.e. don't append the word into the queue.
# # if the word not in the visited map, we put the word into the map, and append the word into the queue.
