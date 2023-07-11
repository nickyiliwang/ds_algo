from typing import *
from ds_types.linked_list import LinkedList, ListNode

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1str = ""
        l2str = ""

        while l1:
            l1str = str(l1.val) + l1str
            l1 = l1.next
        while l2:
            l2str = str(l2.val) + l2str
            l2 = l2.next

        sum = int(l1str) + int(l2str)
        sum = str(sum)

        dummy = ListNode()
        curr = dummy

        for n in reversed(sum):
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next


# # NONE optimal solution
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         list1 = []
#         list2 = []

#         while l1:
#             list1.append(l1.val)
#             l1 = l1.next

#         while l2:
#             list2.append(l2.val)
#             l2 = l2.next

#         str1 = ""
#         str2 = ""

#         for n in reversed(list1):
#             str1 = str1 + str(n)

#         for n in reversed(list2):
#             str2 = str2 + str(n)

#         sum = int(str1) + int(str2)

#         resList = LinkedList()

#         for n in reversed(str(sum)):
#             resList.append(int(n))

#         return resList.head.next


# list1 = LinkedList()
# list1.append(2)
# list1.append(4)
# list1.append(3)

# list2 = LinkedList()
# list2.append(5)
# list2.append(6)
# list2.append(4)

# print(
#     Solution.addTwoNumbers("", list1.head.next, list2.head.next)
# )