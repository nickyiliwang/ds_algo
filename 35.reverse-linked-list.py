from typing import Optional


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

    # display curr_node contents
    def display(self):
        elements = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elements.append(curr_node.data)
        print(elements)


def reverseList(head: Optional[linked_list]) -> Optional[linked_list]:
    print(head)

# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}


my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()

reverseList(my_list.head)
