class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        carry = 0

        while l1 or l2:
            d = carry
            if l1 and l2:
                d += (l1.val+l2.val)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                d += l1.val
                l1 = l1.next
            elif l2:
                d += l2.val
                l2 = l2.next
            carry = d // 10
            cur.next = ListNode(d%10)
            cur = cur.next
        if carry : cur.next = ListNode(1)
        return dummy.next
