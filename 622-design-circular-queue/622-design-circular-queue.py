class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.k = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.k == self.size:
            return False
        self.k += 1
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return True

    def deQueue(self) -> bool:
        if self.k == 0:
            return False
        self.k -= 1
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return True

    def Front(self) -> int:
        if self.k == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.k == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.k == 0

    def isFull(self) -> bool:
        return self.k == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()