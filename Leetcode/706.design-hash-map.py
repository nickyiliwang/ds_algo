#
# @lc app=leetcode id=706 lang=python
#
# [706] Design HashMap
#
# https://leetcode.com/problems/design-hashmap/description/
#
# algorithms
# Easy (65.88%)
# Likes:    4986
# Dislikes: 449
# Total Accepted:    547.5K
# Total Submissions: 831.2K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get","remove","get"]\n' + '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If
# the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or
# -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map
# contains the mapping for the key.
#
#
#
# Example 1:
#
#
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
#
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1],
# [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the
# existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now
# [[1,1]]
#
#
#
# Constraints:
#
#
# 0 <= key, value <= 10^6
# At most 10^4 calls will be made to put, get, and remove.
#
#
#


# @lc code=start
class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap(object):
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def currNode(self, key):
        return self.map[key % 1000]

    def put(self, key, value):
        curr = self.currNode(key)
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next

        curr.next = ListNode(key, value)

    def get(self, key):
        curr = self.currNode(key)

        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next

        return -1

    def remove(self, key):
        curr = self.currNode(key)

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end


# Array only solution
class MyHashMap(object):
    def __init__(self):
        self.arr = []

    def put(self, key, value):
        for i, pair in enumerate(self.arr):
            if pair[0] == key:
                self.arr[i] = [key, value]
                return
        self.arr.append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for pair in self.arr:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                del self.arr[i]
                break
