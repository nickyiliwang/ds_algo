from typing import Optional
from ds_types.linked_list import LinkedList, ListNode


def reorderList(head: Optional[ListNode]) -> None:
    # phase 1
    # using Slow Fast Algo to divide the list into 2 parts
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # phase 2
    # reverse second half
    prev, curr = None, slow
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    # phase 3
    # rearrange the 2 parts into desired linked list
    # weave into the pattern
    first, second = head, prev
    while second.next:
        tmp = first.next
        first.next = second
        first = tmp

        tmp = second.next
        second.next = first
        second = tmp


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
reorderList(linked_list.head)
linked_list.display()
