# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
from typing import Optional
from ds_types.linked_list import LinkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(head: Optional[ListNode]) -> None:
        # phase 1
        # using Slow Fast Algo to divide the list into 2 parts

        # phase 2
        # rearrange the 2 parts into desired linked list

        print(head)


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.display()
