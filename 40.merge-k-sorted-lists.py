from typing import Optional
from typing import List
from ds_types.linked_list import LinkedList

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    print(lists[1].next.val)


list = []
linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(4)
linked_list_1.append(5)
linked_list_2 = LinkedList()
linked_list_2.append(1)
linked_list_2.append(3)
linked_list_2.append(4)
linked_list_3 = LinkedList()
linked_list_3.append(2)
linked_list_3.append(6)
linked_list_1.display()
linked_list_2.display()
linked_list_3.display()
list.append(linked_list_1.head)
list.append(linked_list_2.head)
list.append(linked_list_3.head)

mergeKLists(list)
# linked_list.display()
