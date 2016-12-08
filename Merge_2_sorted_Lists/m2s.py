# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 is not None) and (l2 is not None):
            if l1.val > l2.val:
                head_sol = ListNode(l2.val)
                l2 = l2.next
            else:
                head_sol = ListNode(l1.val)
                l1 = l1.next
        elif (l1 is None) and (l2 is None):
            return None

        elif (l1 is None) and (l2 is not None):
            return l2

        elif (l1 is not None) and (l2 is None):
            return l1

        sol = ListNode(0)
        head_sol.next = sol

        k = 1
        while (k == 1):
            if (l1 is not None) and (l2 is not None):
                val1 = l1.val
                val2 = l2.val
                if val1 > val2:
                    sol.val = val2
                    l2 = l2.next
                else:
                    sol.val = val1
                    l1 = l1.next
            elif (l1 is None):
                sol.val = l2.val
                l2 = l2.next
            elif (l2 is None):
                sol.val = l1.val
                l1 = l1.next

            if (l1 is None) and (l2 is None):
                break
            sol.next = ListNode(0)
            sol = sol.next
        return head_sol
