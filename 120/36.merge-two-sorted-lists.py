class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    # avoid initial empty list edge case by having a dummy
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        # list1 value needs to be smaller, because we start small
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        # after either append, tail go next
        tail = tail.next

    # appending what's left of either list
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    # not returning tail, because we are skipping the dummy
    return dummy.next


mergeTwoLists()
