# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
from typing import Optional
from ds_types.linked_list import LinkedList


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    # phase 1
    # using Slow Fast Algo to divide the list into 2 parts
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # fast.val will sometimes be None if List has even numbers
    # print(slow.val, fast)

    # phase 2
    # reverse second half
    # left pointer
    prev = None

    # curr
    second = slow.next
    # if slow.val = 3
    # slow.next.val = 4
    # to reverse the second half we take the head node of second part (3)
    # and reverse the pointer to None

    # here we split the second half off from first half
    slow.next = None

    while second:
        # temp next node
        tmp = second.next
        second.next = prev
        # shift pointers
        prev = second
        second = tmp

    # phase 3
    # rearrange the 2 parts into desired linked list
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.display()
reorderList(linked_list.head)
linked_list.display()
