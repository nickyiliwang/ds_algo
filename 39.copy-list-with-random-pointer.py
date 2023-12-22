from typing import *
from collections import *
from math import *
from ds_types.linked_list import LinkedList, ListNode


class Solution(object):
    def copyRandomList(self, head):
        copyOldLink = {None: None}

        curr = head

        while curr:
            copy = Node(curr.val)
            copyOldLink[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = copyOldLink[curr]
            copy.next = copyOldLink[curr.next]
            copy.random = copyOldLink[curr.random]
            curr = curr.next

        return copyOldLink[head]


class Solution(object):
    def copyRandomList(self, head):
        # one of the random val will point to Null, so None mapped to None
        oldToCopy = {None: None}

        curr = head

        # create deep copy of nodes and save to map
        while curr:
            copy = ListNode(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            # directly manipulating the Nodes in the map
            copy = oldToCopy[curr]
            # assign what was in the old link values to the copy
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        # return the head from map with copied Nodes
        return oldToCopy[head]
