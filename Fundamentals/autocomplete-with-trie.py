from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isEnd

    def startsWith(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def findAllWithPrefix(self, prefix: str) -> List[str]:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        return self.find(curr, prefix)

    def find(self, node, prefix):
        found = []
        if node.isEnd:
            found.append(prefix)
        for char, child in node.children.items():
            found.extend(self.find(child, prefix + char))
        return found


# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("cherry")
trie.insert("orange")
trie.insert("octopus")
trie.insert("octane")

# trie.search("apple")  # returns True
# trie.search("app")  # returns False

# print(trie.findAllWithPrefix("app"))
print(trie.findAllWithPrefix("oct"))


# A trie (prefix tree) is a tree-like data structure that is used to store a dynamic set of strings. It allows you to efficiently search for a string in the set by prefix, making it well-suited for tasks such as autocomplete and spell check.

# A binary search tree (BST) is a tree-like data structure that is used to store a dynamic set of elements such that they can be efficiently searched and sorted. It is based on the principle that for any given node in the tree, the value of all the nodes in its left subtree is less than the value of the node, and the value of all the nodes in its right subtree is greater than the value of the node.

# There are several differences between tries and BSTs:

# Tries are used to store strings, while BSTs are used to store elements that can be compared using a total ordering (e.g. integers, floating-point numbers, strings).
# Tries are optimized for prefix search, while BSTs are optimized for search and sorting.
# Tries do not have a strict structure like BSTs, where the left child of a node must be less than the node and the right child must be greater than the node. In a trie, the children of a node are determined by the characters in the strings being stored.
# Tries do not support operations such as finding the minimum or maximum element, or deleting an element. These operations are supported by BSTs.
# Despite these differences, both tries and BSTs are tree-like data structures that are used to store and search for elements in an efficient manner.


# This implementation of a trie has three main methods: insert, which adds a word to the trie; search, which searches for a word in the trie; and findAllWithPrefix, which finds all words in the trie that start with a given prefix.

# To implement the autocomplete input, you can use the findAllWithPrefix method to search for words in the trie that start with the prefix entered by the user, and display these words as suggestions to the user.

# Visualization
#          root
#           |
#          (a)
#         / | \
#      (p) (b) (c)
#     /   |   |   \
#   (p)  (a)  (h)  (h)
#   /   /   /   /   \
#  (l) (n) (e) (r)   (r)
#         |   |   /   /
#        (a) (y) (y) (y)

# Each node in the trie represents a single character in a word. The edges between the nodes represent the relationships between the characters. The root node represents the empty string, and the leaf nodes represent complete words. In this example, the words "apple", "banana", "cherry", and "orange" are stored in the trie.

# To search for a word in the trie, the code starts at the root and follows the path through the tree for each character in the word. If the word is present in the trie, the search will end at a leaf node that is marked as the end of a word. If the word is not present, the search will end at a node that has no children or at a node that is not marked as the end of a word.

# To find all words with a given prefix in the trie, the code starts at the root and follows the path through the tree for each character in the prefix. It then performs a depth-first search of the subtree rooted at the last character of the prefix, collecting all the words in the subtree as it goes.
