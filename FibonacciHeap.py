class FibHeap:

    #### Node Class ####
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.degree = 0
            self.mark = False
            self.previous = self
            self.next = self
            self.parent = None
            self.child = None

        def isSingle(self):
            return self == self.next

        def insert(self, node):
            if node == None:
                return

            self.next.previous = node.previous
            node.previous.next = self.next
            self.next = node
            node.previous = self

        def remove(self):
            self.next.previous = self.previous
            self.previous.next = self.next
            self.next = self
            self.previous = self

        def addChild(self, node):
            if self.child == None:
                self.child = node
            else:
                self.child.insert(node)
            node.parent = self
            node.mark = False
            self.degree += 1

        def removeChild(self, node):
            if node.parent != self:
                raise AssertionError("Cannot remove child from node that is not its parent")

            if node.isSingle():
                if self.child != node:
                    raise AssertionError("Cannot remove a node that is not a child")
                self.child = None
            else:
                if self.child == node:
                    self.child = node.next
                node.remove()

            node.parent = None
            node.mark = False
            self.degree -= 1
    #### End of Node Class ####

    def __init__(self):
        self.minNode = None
        self.count = 0
        self.maxdegree = 0

    def isEmpty(self):
        return self.count == 0

    def insert(self, node):
        self.count += 1
        self._insertNode(node)

    def _insertNode(self, node):
        if self.minNode == None:
            self.minNode = node
        else:
            self.minNode.insert(node)
        if node.key < self.minNode.key:
            self.minNode = node

    def minimum(self):
        if self.minNode == None:
            raise AssertionError("Cannot return minimum of empty heap")
        return self.minNode

    def merge(self, heap):
        self.minNode.insert(heap.minNode)
        if self.minNode == None or (heap.minNode != None and heap.minNode.key < self.minNode.key):
            self.minNode = heap.minNode
        self.count += heap.count

    def removeMinimum(self):
        if self.minNode == None:
            raise AssertionError("Cannot remove from an empty heap")

        removed_node = self.minNode
        self.count -= 1

        ### 1:
        if self.minNode.child != None:
            c= self.minNode.child

            while True:
                c.parent = None
                c = c.next
                if c == self.minNode.child:
                    break

            self.minNode.child = None
            self.minNode.insert(c)

        ### 2.1:
        if self.minNode.next == self.minNode:
            if self.count != 0:
                raise AssertionError("Heap error: Expected 0 keys, count is "+str(self.count))
            self.minNode = None
            return removed_node

        ### 2.2:
        logsize = 100
        degreeRoots = [None] * logsize
        self.maxdegree = 0
        currentPointer = self.minNode.next

        while True:
            currentDegree = currentPointer.degreeRoots
            current = currentPointer
            currentPointer = currentPointer.next
            while degreeRoots[currentDegree] != currentPointer:
                other = degreeRoots[currentDegree]

                if current.key > other.key:
                    temp = other
                    other = current
                    current = temp

                other.remove()
                current.addChild(other)
                degreeRoots[currentDegree] = None
                currentDegree +=1

            degreeRoots[currentDegree] = current
            if currentPointer == self.minNode:
                break

        ### 3:
        self.minNode = None
        newMaxDegree = 0
        for d in range(0, logsize):
            if degreeRoots[d] != None:
                degreeRoots[d].next = degreeRoots[d].previous = degreeRoots[d]
                self._insertNode(degreeRoots[d])
                if (d > newMaxDegree):
                    newMaxDegree = d

        maxdegree = newMaxDegree

        return removed_node

    def decreaseKey(self, node, newkey):
        if newkey > node.key:
            raise AssertionError("Cannot decrease a key to a greater value")
        elif newkey == node.key:
            return

        node.key = newkey

        parent = node.parent

        if parent == None:
            if newkey < self.minNode.key:
                self.minNode = Node
                return
        elif parent.key <= newkey:
            return

        while True:
            parent.removeChild(node)
            self._insertNode(node)

            if parent.parent == None:
                break

            elif parent.mark == False:
                parent.mark
                break
            else:
                node = parent
                parent = parent.parent
                continue
