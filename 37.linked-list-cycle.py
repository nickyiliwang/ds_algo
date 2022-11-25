# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.


# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
from ds_types.linked_list import LinkedList
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(1), Space: O(1)
# Tortoise and Hare algo

def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False

# # Time: O(n), Space: O(n)

# def hasCycle(head: Optional[ListNode]) -> bool:
#     # with python set
#     validationHashSet = set()

#     curr = head

#     while curr:
#         if (curr not in validationHashSet):
#             validationHashSet.add(curr)
#         else:
#             return True

#         curr = curr.next

#     return False


linked_list = LinkedList()
repeatingNode = ListNode(5)
# This is not the right way to simulate the data
# we need Node 1 => Node 2 => Node 1
linked_list.append(1)
linked_list.append(2)
linked_list.append(repeatingNode)
linked_list.append(4)
linked_list.append(repeatingNode)
linked_list.display()

print(hasCycle(linked_list.head))
