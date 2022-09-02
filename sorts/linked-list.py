class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    # display current contents
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                print(cur_node.data)
                return cur_node.data
            cur_node += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range")
            return
        cur_index = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                # instead of erasing the element, we are just dropping it from the link
                last_node.next = cur_node.next
                return
            cur_index += 1


my_list = linked_list()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
my_list.get(0)
my_list.erase(3)
my_list.display()
