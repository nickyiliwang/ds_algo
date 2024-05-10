# @lc app=leetcode id=138 lang=python3


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


# @lc code=start
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # one of the random val might point to Null, so None mapped to None
        db = {None: None}

        curr = head
        # create deep copy of nodes and save to map
        while curr:
            n = Node(curr.val)
            db[curr] = n
            curr = curr.next

        curr = head
        while curr:
            n = db[curr]
            # point to nodes in the db with original head's next and random values
            n.next = db[curr.next]
            n.random = db[curr.random]
            curr = curr.next

        return db[head]


# @lc code=end
