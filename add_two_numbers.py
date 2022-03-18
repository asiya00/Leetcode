class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp1 = l1
        temp2 = l2
        ans = []
        while temp1 and temp2:
            a = temp1.val + temp2.val
            if carry:
                a += carry
                carry = 0
            if len(str(a)) > 1:
                carry = int(str(a)[:-1])
            ans.append(int(str(a)[-1]))
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1:
            if carry:
                a = carry + temp1.val
                carry = 0
                if len(str(a)) > 1:
                    carry = int(str(a)[:-1])
                ans.append(int(str(a)[-1]))
            else:
                ans.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            if carry:
                a = carry + temp2.val
                carry = 0
                if len(str(a)) > 1:
                    carry = int(str(a)[:-1])
                ans.append(int(str(a)[-1]))
            else:
                ans.append(temp2.val)
            temp2 = temp2.next
        if carry:
            ans.append(carry)
        
        def makelinkedlist(ans):
            li3 = ListNode(ans[0])
            for i in ans[1:]:
                temp = li3
                while temp.next:
                    temp = temp.next
                temp.next = ListNode(i)
            return li3
        return makelinkedlist(ans)