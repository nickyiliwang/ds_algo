class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def append(self, val):
        new_node = ListNode(val)
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def length(self):
        curr_node = self.head
        total = 0
        while curr_node.next != None:
            total += 1
            curr_node = curr_node.next
        return total

    # display curr_node contents
    def display(self):
        elements = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elements.append(curr_node.val)
        print("elements", elements)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range")
            return None
        cur_index = 0
        curr_node = self.head
        while True:
            curr_node = curr_node.next
            if cur_index == index:
                print(curr_node.val)
                return curr_node.val
            curr_node += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range")
            return
        cur_index = 0
        curr_node = self.head

        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if cur_index == index:
                # instead of erasing the element, we are just dropping it from the link
                last_node.next = curr_node.next
                return
            cur_index += 1


# my_list = LinkedList()
# my_list.display()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# my_list.display()
# my_list.get(0)
# my_list.erase(3)
# my_list.display()
