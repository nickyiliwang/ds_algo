from typing import Optional
from ds_types.linked_list import LinkedList

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# two pointers


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # prev node is Null
    # curr to the first head, head is default val of 0
    prev, curr = None, head
    # ie. [1,2,None]

    # since curr is pointed to either the head or the next node, if it's None means we went to the end of the node

    # the point of this loop is to traverse the linked list and swap the previous node with the next node.

    # run through the list only once
    while curr:
        nextNode = curr.next  # val = 1
        # swap the current node's next pointer to the previous Node, since reversing, we start at None
        curr.next = prev  # change the current Node to have a next Node of None

        # save the current Node in the previous variable
        prev = curr

        # done, save the next node in the current variable for the next loop
        curr = nextNode

    return prev


linked_list = LinkedList()
print("head val", linked_list.head.val)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.display()

reversed = reverseList(linked_list.head)

print(reversed.next.val)
