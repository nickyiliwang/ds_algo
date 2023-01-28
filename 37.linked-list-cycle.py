from ds_types.linked_list import LinkedList, ListNode
from typing import Optional

# Time: O(1), Space: O(1)
# Tortoise and Hare
# Eventually the Tortoise will catch up to the Rabbit if there is a cycle


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # if here because we don't want to check the initial loop.
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
