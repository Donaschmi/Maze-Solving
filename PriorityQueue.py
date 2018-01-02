from abc import ABCMeta, abstractmethod
import itertools

from FibonacciHeap import FibHeap
import heapq
import Queue

class PQueue():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __len__(self): pass

    @abstractmethod
    def insert(self, node): pass

    @abstractmethod
    def minimum(self): pass

    @abstractmethod
    def removeMinimum(self): pass

    @abstractmethod
    def decreaseKey(self, node, newPriority): pass

class FibPQ(PQueue):
    def __init__(self):
        self.heap=FibHeap()

    def __len__(self):
        return self.heap.count

    def insert(self, node):
        return self.heap.insert(node)

    def minimum(self):
        return self.heap.minimum()

    def removeMinimum(self):
        return self.heap.removeMinimum()

    def decreaseKey(self, node, newPriority):
        return self.heap.decreaseKey(node, newPriority)

class HeapPQ(PQueue):
    def __init__(self):
        self.pq = []
        self.removed = set()
        self.count = 0

    def __len__(self):
        return self.count

    def insert(self, node):
        entry = node.key, node.value
        if entry in self.removed:
            self.removed.discard(entry)
        heapq.heappush(self.pq, entry)
        self.count += 1

    def minimum(self):
        priority, item = heapq.headpop(self.pq)
        node = FibHeap.Node(priority, item)
        self.insert(node)
        return Node

    def removeMinimum(self):
        while True:
            (priority, item) = heapq.heappop(self.pq)
            if (priority, item) in self.removed:
                self.removed.discard((priority, item))
            else:
                self.count-=1
                return FibHeap.Node(priority, item)

    def remove(self, node):
        entry = node.key, node.value
        if entry not in self.removed:
            self.removed.add(entry)
            self.count-=1

    def decreaseKey(self, node, newPriority):
        self.remove(node)
        node.key = newPriority
        self.insert(node)

class QueuePQ(PQueue):
    def __init__(self):
        self.pq = Queue.PQueue()
        self.removed = set()
        self.count = 0

    def __len__(self):
        return self.count

    def insert(self, node):
        entry = node.key, node.value
        if entry in self.removed:
            self.removed.discard(entry)
        self.pq.put(entry)
        self.count += 1

    def minimum(self):
        (priority, item) = self.pq.get_nowait()
        node = FibHeap.Node(priority, item)
        self.insert(node)
        return node

    def removeMinimum(self):
        while True:
            (priority, item) = self.pq.get_nowait()
            if (priority, item) in self.removed:
                self.removed.discard((priority, item))
            else:
                self.count -= 1
                return FibHeap.Node(priority, item)

    def remove(self, node):
        entry = node.key, node.value
        if entry not in self.removed:
            self.removed.add(entry)
            self.count-= 1

    def decreaseKey(self, node, newPriority):
        self.remove(node)
        node.key = newPriority
        self.insert(node)
