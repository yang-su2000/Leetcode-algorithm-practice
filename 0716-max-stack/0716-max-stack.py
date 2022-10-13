from sortedcontainers import SortedDict

class Node:
    
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val
        
    # assume l and r both non-empty
    def delete(self):
        self.l.r = self.r
        self.r.l = self.l
        return self.val

class MaxStack:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.r = self.tail
        self.tail.l = self.head
        self.d = SortedDict()
        self.b = 0 # debug

    def add_tail(self, val):
        l = self.tail.l
        r = self.tail
        node = Node(val)
        node.l = l
        l.r = node
        r.l = node
        node.r = r
        return node
        
    def remove_tail(self):
        node = self.tail.l
        return node.delete()
        
    def push(self, x: int) -> None:
        node = self.add_tail(x)
        if x in self.d:
            self.d[x].append(node)
        else:
            self.d[x] = [node]
        if self.b:
            print('push')
            self.debug()

    def pop(self) -> int:
        val = self.remove_tail()
        nodes = self.d[val]
        node = nodes.pop()
        if not nodes:
            del self.d[val]
        del node
        if self.b:
            print('pop')
            self.debug()
        return val

    def top(self) -> int:
        node = self.tail.l
        return node.val

    def peekMax(self) -> int:
        val, nodes = self.d.peekitem()
        return val

    def popMax(self) -> int:
        val, nodes = self.d.peekitem()
        node = nodes.pop()
        if not nodes:
            del self.d[val]
        node.delete()
        del node
        if self.b:
            print('popMax')
            self.debug()
        return val
                
    def debug(self):
        for val, nodes in self.d.items():
            print(val, 'x', len(nodes), end=' | ')
        print()


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()