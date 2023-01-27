from typing import Optional
from ds_types.linked_list import LinkedList, ListNode


def reorderList(head: Optional[ListNode]) -> None:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

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
linked_list.append(5)
linked_list.append(6)
reorderList(linked_list.head)
linked_list.display()


# def linkedListManipulate(head: Optional[ListNode]) -> Optional[ListNode]:
#     node = ListNode(7, None)
#     while head.next:
#         head = head.next
#     head.next = node


# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.append(5)
# linked_list.append(6)
# linkedListManipulate(linked_list.head)
# linked_list.display()
