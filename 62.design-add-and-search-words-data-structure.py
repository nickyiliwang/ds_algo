#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (44.78%)
# Likes:    7391
# Dislikes: 433
# Total Accepted:    597.6K
# Total Submissions: 1.3M
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched
# later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
#
#
#
# Example:
#
#
# Input
#
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.
#
#
#


# @lc code=start
class TriNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TriNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TriNode()

            curr = curr.children[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            if index == len(word):  # base case
                return root.isEnd

            curr = root
            char = word[index]
            if char == ".":
                for child in curr.children.values():
                    if dfs(index + 1, child):
                        return True

            if char in root.children:
                return dfs(index + 1, root.children[char])

            return False

        return dfs(0, self.root)

    # @lc code=end


# NONE recursive search
# 3/29 cases passed
def search(self, word: str) -> bool:
    curr = self.root
    for index, char in enumerate(word):
        if char == ".":
            listOfCurrChildren = curr.children.values()
            for child in listOfCurrChildren:
                currCharIdx = index + 1
                while currCharIdx < len(word) - 1:
                    if word[currCharIdx] not in child.children:
                        continue

                    currCharIdx += 1
                return child.isEnd
            return False
        else:
            if char not in curr.children:
                return False


# Example usage
dictionary = WordDictionary()
dictionary.addWord("apple")
dictionary.addWord("banana")
dictionary.addWord("cherry")
dictionary.addWord("orange")
dictionary.addWord("octopus")
dictionary.addWord("octane")
