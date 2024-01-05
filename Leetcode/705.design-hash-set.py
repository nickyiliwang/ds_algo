#
# @lc app=leetcode id=705 lang=python
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (67.08%)
# Likes:    3681
# Dislikes: 298
# Total Accepted:    386.1K
# Total Submissions: 575.7K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' + '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or
# not.
# void remove(key) Removes the value key in the HashSet. If key does not exist
# in the HashSet, do nothing.
#
#
#
# Example 1:
#
#
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
#
#
# Constraints:
#
#
# 0 <= key <= 10^6
# At most 10^4 calls will be made to add, remove, and contains.
#
#
#


# @lc code=start
class MyHashSet(object):
    def __init__(self):
        self.set = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.set:
            self.set[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.set:
            return self.set[key]
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end


# # You can certainly solve the HashSet problem using a linked list approach. However, it's important to note that the time complexity of the operations will be different compared to using a hash table.

# # In a linked list approach, you can use a singly linked list where each node represents a value in the HashSet. To add a value, you would traverse the linked list to check if the value already exists. If not, you would add a new node at the end of the list. To remove a value, you would again traverse the list to find the node with the target value and remove it by updating the pointers. To check if a value exists, you would traverse the list and compare each node's value with the target value.

# # The time complexity for adding a value in this approach would be O(n), where n is the number of elements in the linked list. Similarly, the time complexity for removing and checking if a value exists would also be O(n). This is because you may need to traverse the entire linked list in the worst case scenario.

# # On the other hand, using a hash table allows for constant-time operations on average (O(1)) for adding, removing, and checking if a value exists. This is because a hash table uses a hashing function to map keys to indices, allowing for efficient lookup and insertion.

# # So, while a linked list approach is feasible for implementing a HashSet, it may not provide the same level of performance as a hash table implementation.


# # Overall, linked lists are most appropriate when dynamic resizing, frequent insertion/deletion, memory allocation considerations, or simplicity of implementation are important factors in your specific use case.


class ListNode:
    def __init__(self, value=-1, next=None):
        self.value = value
        self.next = next


class MyHashSet(object):
    def __init__(self):
        self.head = ListNode()

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        curr = self.head
        while curr.next:
            if curr.value == value or curr.next.value == value:
                return
            curr = curr.next
        curr.next = ListNode(value)

    def remove(self, value):
        """
        :type value: int
        :rtype: None
        """
        curr = self.head
        while curr.next:
            if curr.next.value == value:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, value):
        """
        :type value: int
        :rtype: bool
        """
        curr = self.head
        while curr.next:
            if curr.next.value == value:
                return True
            curr = curr.next
        return False

    def printList(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        print(res)
