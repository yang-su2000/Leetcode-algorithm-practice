"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def rec(self, head):
        # print(head.val)
        l_cur = head
        r_cur = head
        while head:
            r_cur = head
            if head.child:
                l = head
                r = head.next
                l_next, r_prev = self.rec(head.child)
                l.next = l_next
                l_next.prev = l
                r_prev.next = r
                if r:
                    r.prev = r_prev
                r_cur = r_prev
                head.child = None
                head = r
            else:
                head = head.next
        # print(l_cur.val, r_cur.val)
        return l_cur, r_cur
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.rec(head)
        return head