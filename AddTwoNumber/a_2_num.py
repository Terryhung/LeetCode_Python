# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        first_node = ListNode(0)
        overflow = 0
        curry_node = first_node
        while (l1 is not None) or (l2 is not None):
            if l1 is not None:
                x = l1.val
            else:
                x = 0

            if l2 is not None:
                y = l2.val
            else:
                y = 0

            _sum = x + y + overflow

            if _sum > 9:
                _val = _sum - 10
                overflow = 1

            else:
                _val = _sum
                overflow = 0

            curry_node.next = ListNode(_val)
            curry_node = curry_node.next

            if (l1 is not None):
                l1 = l1.next
            else:
                l1 = None

            if (l2 is not None):
                l2 = l2.next
            else:
                l2 = None

        if overflow > 0:
            curry_node.next = ListNode(1)

        return first_node.next
