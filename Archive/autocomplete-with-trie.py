from typing import List

# This implementation of a trie has three main methods: insert, which adds a word to the trie; search, which searches for a word in the trie; and find_words_with_prefix, which finds all words in the trie that start with a given prefix.

# To implement the autocomplete input, you can use the find_words_with_prefix method to search for words in the trie that start with the prefix entered by the user, and display these words as suggestions to the user.

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


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def find_words_with_prefix(self, prefix: str) -> List[str]:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]
        return self._find_all_words(curr, prefix)

    def _find_all_words(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append(prefix)
        for ch, child in node.children.items():
            child_prefix = prefix + ch
            result.extend(self._find_all_words(child, child_prefix))
        print(result)
        return result


# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("cherry")
trie.insert("orange")
trie.insert("octopus")

trie.search("apple")  # returns True
trie.search("app")  # returns False

trie.find_words_with_prefix("app")  # returns ["apple"]
trie.find_words_with_prefix("o")  # returns ["orange"]

# A trie (prefix tree) is a tree-like data structure that is used to store a dynamic set of strings. It allows you to efficiently search for a string in the set by prefix, making it well-suited for tasks such as autocomplete and spell check.

# A binary search tree (BST) is a tree-like data structure that is used to store a dynamic set of elements such that they can be efficiently searched and sorted. It is based on the principle that for any given node in the tree, the value of all the nodes in its left subtree is less than the value of the node, and the value of all the nodes in its right subtree is greater than the value of the node.

# There are several differences between tries and BSTs:

# Tries are used to store strings, while BSTs are used to store elements that can be compared using a total ordering (e.g. integers, floating-point numbers, strings).
# Tries are optimized for prefix search, while BSTs are optimized for search and sorting.
# Tries do not have a strict structure like BSTs, where the left child of a node must be less than the node and the right child must be greater than the node. In a trie, the children of a node are determined by the characters in the strings being stored.
# Tries do not support operations such as finding the minimum or maximum element, or deleting an element. These operations are supported by BSTs.
# Despite these differences, both tries and BSTs are tree-like data structures that are used to store and search for elements in an efficient manner.