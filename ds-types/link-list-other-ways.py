class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while True:
            # reached tail
            if curr_node.next is None:
                curr_node.next = new_node
                break
            # setting current node to the next node
            # so we can keep traversing to tail
            curr_node = curr_node.next

    def pop(self):
        if self.head is None:
            return

        prev_node = None
        curr_node = self.head

        while curr_node.next is not None:
            prev_node = curr_node

            # limiting condition
            # to keep traversing till tail
            curr_node = curr_node.next

        prev_node.next = None

    def display(self):
        curr_node = self.head
        elements = []
        while curr_node is not None:
            elements.append(curr_node.data)
            curr_node = curr_node.next
        print(elements)


my_list = linked_list()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.pop()
my_list.pop()

my_list.display()
