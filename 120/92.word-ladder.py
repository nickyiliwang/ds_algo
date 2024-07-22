#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
#
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
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
from collections import defaultdict, deque
from typing import List


# BigO n^2 * M

# Key:
# word[:i] + "*" + word[i + 1:]
# need an adjacency list for patterns
# BFS with deq
# need a visited set bc to check sequence
# 

# hot: *ot, h*t, ho*
# dot: *ot, d*t, do*
# lot: *ot, l*t, lo*
# {*ot: [hot, dot, lot]}

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        wordList.append(beginWord)
        q = deque([beginWord])
        res = 1
        visited = set()

        # Build adjacency list
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1 :]
                graph[pattern].append(w)

        # BFS check each level to find the endWord
        while q:
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return res

                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i + 1 :]
                    # Ref pattern in adjList, only want unvisited
                    for word in graph[pattern]:
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
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


# As we can see,  "hot" has been visited in level 2, but "hot" will still appear at the next level.
# To avoid duplicate calculation,
# we keep a visited map,
# if the word in the visited map, we skip the word, i.e. don't append the word into the queue.
# if the word not in the visited map, we put the word into the map, and append the word into the queue.
