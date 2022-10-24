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
    def rec(self, prev, cur):
        if not cur:
            return prev
        cur.prev = prev
        prev.next = cur
        tmp_next = cur.next
        tail = self.rec(cur, cur.child)
        cur.child = None
        return self.rec(tail, tmp_next)
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        dummy = Node(None, None, head, None)
        self.rec(dummy, head)
        dummy.next.prev = None
        return dummy.next