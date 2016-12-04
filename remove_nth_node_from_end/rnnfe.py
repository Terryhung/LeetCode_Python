# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def check_LenOfNode(node):
    if node is not None:
        _len = 1
        while(node.next is not None):
            _len = _len + 1
            node = node.next
        return _len
    else:
        return 0


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        _len = check_LenOfNode(head)
        removed_index = _len - n + 1
        if removed_index == 1:
            return head.next

        counter = 1
        present_node = head
        old_node = None
        for _index in range(1, _len+1):
            if counter != removed_index:
                old_node = present_node
                present_node = present_node.next
                counter = counter + 1
            else:
                old_node.next = present_node.next
                break

        return head
