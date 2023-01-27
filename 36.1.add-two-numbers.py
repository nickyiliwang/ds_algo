class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        for i in range(len(sum) -1, -1, -1):
            curr.next = ListNode(int(sum[i]))
            curr = curr.next
            
        return dummy.next