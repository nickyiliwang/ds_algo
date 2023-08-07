from typing import Optional, List
from ds_types.linked_list import LinkedList, ListNode

# BigO(n log K)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # checking for empty array edge cases
        if not lists or len(lists) == 0:
            return None

        # Keep going until 1 list remain
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # ensure we only process and merge even lists
                # len(lists) > (i + 1): the remaining list should at least be 2 lists
                l2 = lists[i + 1] if len(lists) > (i + 1) else None

                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next


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

mergeKListsInstance = Solution()

newList = mergeKListsInstance.mergeKLists(list)

while newList:
    print(newList.val)
    newList = newList.next
